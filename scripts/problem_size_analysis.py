"""Analyze performance of synthesized programs vs problem size."""

import argparse
import os
import pickle
import re
import subprocess
import tempfile
import time
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, Iterator, List, Optional, Set, Tuple

import matplotlib
import numpy as np
from analyze_results import load_results
from matplotlib import pyplot as plt

from llm_genplan import utils
from llm_genplan.envs.assets.pddl.pg3.heavypack_problem_gen import _run as heavypack_gen
from llm_genplan.genplan import GeneralizedPlan
from llm_genplan.structs import Metrics, Task

ENV_TO_LABEL = {
    "pg3-heavypack": "Heavy",
    "pg3-hiking": "Forest",
    "pg3-trapnewspapers": "Delivery",
    "pg3-manymiconic": "Miconic",
    "pg3-manygripper": "Gripper",
    "pg3-manyferry": "Ferry",
    "pg3-spannerlearning": "Spanner",
}

APPROACH_TO_LABEL = {
    "chatgpt4": "GPT-4",
    "fd-lama-first": "Fast Downward",
}


def _main() -> None:
    matplotlib.rcParams.update({"font.size": 16})
    pickle_filepath = Path("problem_size_analysis_results.p")
    plot_filepath = Path("problem_size_analysis.png")
    if not pickle_filepath.exists():
        # Load raw results.
        parser = argparse.ArgumentParser()
        parser.add_argument("--results_dir", default="results", type=str)
        args = parser.parse_args()
        gen_plan_results, _ = load_results(args.results_dir)
        # Determine which domains were at least 50% successful for chatgpt4 and
        # which of the seeds for those domains were successes.
        main_results = gen_plan_results.loc[
            gen_plan_results.experiment_id == "chatgpt4"
        ]
        env_to_success_seeds: DefaultDict[str, Set[int]] = defaultdict(set)
        for _, row in main_results.iterrows():
            # TODO
            if row.env != "pg3-heavypack":
                continue
            if row.success_rate > 1.0 - 1e-6:
                env_to_success_seeds[row.env].add(int(row.seed))
        num_seeds = len(set(main_results.seed))
        for env in set(env_to_success_seeds):
            if len(env_to_success_seeds[env]) < num_seeds / 2:
                del env_to_success_seeds[env]
        # Generate results for each remaining env.
        results: Dict[str, Tuple[List[int], Dict[str, List[List[List[float]]]]]] = {}
        for env in sorted(env_to_success_seeds):
            seeds = env_to_success_seeds[env]
            env_xs, approach_to_env_ys = _run_single_env(env, seeds)
            results[env] = (env_xs, approach_to_env_ys)
        # Save the results.
        with open(pickle_filepath, "wb") as f:
            pickle.dump(results, f)
    else:
        with open(pickle_filepath, "rb") as f:
            results = pickle.load(f)
    # Make plots.
    _generate_plots(results, plot_filepath)


def _run_single_env(
    env: str, seeds: Set[int]
) -> Tuple[List[int], Dict[str, List[List[List[float]]]]]:
    env_xs: Optional[List[int]] = None
    approach_to_env_ys: Dict[str, List[List[List[float]]]] = {
        "chatgpt4": [],
        "fd-lama-first": [],
    }
    for seed in sorted(seeds):
        # Load the genplan for this seed.
        genplan = _load_genplan(env, seed)
        # Generate and evaluate on problems.
        for approach in approach_to_env_ys:
            approach_to_env_ys[approach].append([])
        seed_env_xs: List[int] = []
        for x, tasks_x in _generate_varying_size_tasks(env, seed):
            seed_env_xs.append(x)
            for approach in sorted(approach_to_env_ys):
                print(f"Evaluating {approach} on {env} tasks of size {x}")
                approach_to_env_ys[approach][-1].append([])
                for task in tasks_x:
                    if approach == "chatgpt4":
                        start_time = time.perf_counter()
                        plan = genplan.run(task)
                        duration = time.perf_counter() - start_time
                    else:
                        assert approach == "fd-lama-first"
                        plan, metrics = run_fastdownward_planning(task)
                        duration = metrics["duration"]
                    # Validate the plan.
                    success, _ = utils.validate_plan(task, plan)
                    # Handle infs later.
                    if not success:
                        duration = float("inf")
                    approach_to_env_ys[approach][-1][-1].append(duration)
        if env_xs is None:
            env_xs = seed_env_xs
        assert env_xs == seed_env_xs
    assert env_xs is not None
    return env_xs, approach_to_env_ys


def _load_genplan(
    env: str, seed: int, experiment_id: str = "chatgpt4"
) -> GeneralizedPlan:
    save_dir = utils.CACHE_DIR / f"{env}_{seed}_{experiment_id}"
    responses = save_dir.glob("*-response.txt")
    last_response_path = max(responses, key=lambda r: int(r.stem.split("-")[0]))
    with open(last_response_path, "r", encoding="utf-8") as f:
        code_str = f.read()
    return GeneralizedPlan(code_str)


def _generate_varying_size_tasks(
    env: str, seed: int, num_tasks_per_size: int = 10
) -> Iterator[Tuple[int, List[Task]]]:
    # Heavypack
    if env == "pg3-heavypack":
        all_num_items = [1, 4, 16, 64, 256, 1024]
        domain_filepath = utils.PDDL_DIR / "pg3" / "heavypack.pddl"
        with open(domain_filepath, "r", encoding="utf-8") as f:
            domain_str = f.read()
        with tempfile.TemporaryDirectory() as td:
            temp_dir = Path(td)
            for num_items in all_num_items:
                heavypack_gen(
                    train_dir=temp_dir,
                    test_dir=temp_dir,
                    num_seed=1,
                    num_train_per_seed=0,
                    num_test_per_seed=num_tasks_per_size,
                    test_min_num_items=num_items,
                    test_max_num_items=num_items,
                    seed_offset=seed,
                )
                seed_dir = temp_dir / f"seed{seed}"
                tasks: List[Task] = []
                for pddl_file in seed_dir.glob("*.pddl"):
                    with open(pddl_file, "r", encoding="utf-8") as f:
                        problem_str = f.read()
                    task = Task(domain_str, problem_str)
                    tasks.append(task)
                assert len(tasks) == num_tasks_per_size
                yield (num_items, tasks)

    else:
        import ipdb

        ipdb.set_trace()


def run_fastdownward_planning(
    task: Task,
    alias: Optional[str] = "lama-first",
    search: Optional[str] = None,
    timeout: int = 30,
) -> Tuple[List[str], Metrics]:
    """Find a plan with fast downward.

    Usage: Build and compile the Fast Downward planner, then set the environment
    variable FD_EXEC_PATH to point to the `downward` directory. For example:
    1) git clone https://github.com/ronuchit/downward.git
    2) cd downward && ./build.py
    3) export FD_EXEC_PATH="<your absolute path here>/downward"

    Also make sure python3.9 is installed.
    """
    # Specify either a search flag or an alias.
    assert (search is None) + (alias is None) == 1
    # The SAS file isn't actually used, but it's important that we give it a
    # name, because otherwise Fast Downward uses a fixed default name, which
    # will cause issues if you run multiple processes simultaneously.
    sas_file = tempfile.NamedTemporaryFile(delete=False).name
    # Run Fast Downward followed by cleanup. Capture the output.
    assert (
        "FD_EXEC_PATH" in os.environ
    ), "Please follow the instructions in the docstring of this method!"
    if alias is not None:
        alias_flag = f"--alias {alias}"
    else:
        alias_flag = ""
    if search is not None:
        search_flag = f"--search '{search}'"
    else:
        search_flag = ""
    fd_exec_path = os.environ["FD_EXEC_PATH"]
    exec_str = os.path.join(fd_exec_path, "fast-downward.py")
    cmd_str = (
        f'python3.9 "{exec_str}" {alias_flag} '
        f"--overall-time-limit {timeout} "
        f"--sas-file {sas_file} "
        f'"{task.domain_file}" "{task.problem_file}" '
        f"{search_flag}"
    )
    output = subprocess.getoutput(cmd_str)
    cleanup_cmd_str = f"{exec_str} --cleanup"
    subprocess.getoutput(cleanup_cmd_str)
    # Parse and log metrics.
    if "Time limit has been reached" in output:
        num_nodes_expanded = re.findall(r"(\d+) expanded", output)[-1]
        num_nodes_created = re.findall(r"(\d+) evaluated", output)[-1]
        duration = float(timeout)
    else:
        num_nodes_expanded = re.findall(r"Expanded (\d+) state", output)[0]
        num_nodes_created = re.findall(r"Evaluated (\d+) state", output)[0]
        total_time = re.findall(r"Total time: (\d+\.\d+)", output)[0]
        duration = float(total_time)
    metrics = {
        "nodes_expanded": float(num_nodes_expanded),
        "nodes_created": float(num_nodes_created),
        "duration": duration,
    }
    # Extract the plan from the output, if one exists.
    if "Solution found!" not in output:
        return [], metrics
    if "Plan length: 0 step" in output:
        # Handle the special case where the plan is found to be trivial.
        return [], metrics
    plan_str = re.findall(r"(.+) \(\d+?\)", output)
    assert plan_str  # already handled empty plan case, so something went wrong
    plan = [f"({a})" for a in plan_str]
    return plan, metrics


def _generate_plots(
    results: Dict[str, Tuple[List[int], Dict[str, List[List[List[float]]]]]],
    outfile_path: Path,
) -> None:
    num_subplots = len(results)
    with plt.style.context("bmh"):
        fig, _ = plt.subplots(1, num_subplots)
        for ax, env in zip(fig.axes, sorted(results)):
            env_xs, approach_to_env_ys = results[env]
            for approach in sorted(approach_to_env_ys):
                env_ys = approach_to_env_ys[approach]  # (seeds, objects, tasks)
                mean_env_ys = np.mean(env_ys, axis=(0, 2))
                assert len(env_xs) == len(mean_env_ys)
                ax.plot(
                    env_xs, mean_env_ys, marker="o", label=APPROACH_TO_LABEL[approach]
                )
            ax.set_title(ENV_TO_LABEL[env])
            ax.set_xticks(env_xs)
            ax.set_xlabel("# Objects")
            ax.set_ylabel("Planning Time (s)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(outfile_path)
    print(f"Wrote out to {outfile_path}")


if __name__ == "__main__":
    _main()
