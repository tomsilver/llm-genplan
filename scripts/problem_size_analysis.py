"""Analyze performance of synthesized programs vs problem size."""

import argparse
import pickle
import random
import tempfile
import time
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, Iterator, List, Optional, Set, Tuple

import matplotlib
import numpy as np
from analyze_results import load_results
from matplotlib import pyplot as plt
from pddlgym.parser import PDDLDomainParser

from llm_genplan import utils
from llm_genplan.envs.assets.pddl.pg3.heavypack_problem_gen import _run as heavypack_gen
from llm_genplan.genplan import GeneralizedPlan
from llm_genplan.structs import Task
from llm_genplan.third_party.pg3_gen.hikingpg import create_problem as hiking_gen
from llm_genplan.third_party.pg3_gen.hikingpg import generate_random_grid
from llm_genplan.third_party.pg3_gen.manyferrypg import _get_str as ferry_gen
from llm_genplan.third_party.pg3_gen.manygripperpg import sample_problem as gripper_gen
from llm_genplan.third_party.pg3_gen.trapnewspaperspg import sample_problem as news_gen

ENV_TO_LABEL = {
    "pg3-heavypack": "Heavy",
    "pg3-hiking": "Forest",
    "pg3-trapnewspapers": "Delivery",
    "pg3-manygripper": "Gripper",
    "pg3-manyferry": "Ferry",
}

ENV_ORDER = [
    "pg3-trapnewspapers",
    "pg3-hiking",
    "pg3-manygripper",
    "pg3-manyferry",
    "pg3-heavypack",
]

APPROACH_TO_LABEL = {
    "chatgpt4": "GPT-4",
    "fd-lama-first": "Fast Downward",
}

TIMEOUT = 30


def _main() -> None:
    matplotlib.rcParams.update({"font.size": 32})
    plot_filepath = Path("problem_size_analysis.png")
    # Load raw results.
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", default="results", type=str)
    args = parser.parse_args()
    gen_plan_results, _ = load_results(args.results_dir)
    # Determine which domains were at least 50% successful for chatgpt4 and
    # which of the seeds for those domains were successes.
    main_results = gen_plan_results.loc[gen_plan_results.experiment_id == "chatgpt4"]
    env_to_success_seeds: DefaultDict[str, Set[int]] = defaultdict(set)
    for _, row in main_results.iterrows():
        if row.success_rate > 1.0 - 1e-6:
            env_to_success_seeds[row.env].add(int(row.seed))
    num_seeds = len(set(main_results.seed))
    for env in set(env_to_success_seeds):
        if len(env_to_success_seeds[env]) < num_seeds / 2:
            del env_to_success_seeds[env]
    # Generate results for each remaining env.
    results: Dict[str, Tuple[List[int], Dict[str, List[List[List[float]]]]]] = {}
    for env in sorted(env_to_success_seeds):
        pickle_filepath = Path(f"{env}_problem_size_analysis_results.p")
        if pickle_filepath.exists():
            with open(pickle_filepath, "rb") as f:
                env_results = pickle.load(f)
        else:
            seeds = env_to_success_seeds[env]
            env_results = _run_single_env(env, seeds)
            # Save the results.
            with open(pickle_filepath, "wb") as f:
                pickle.dump(env_results, f)
        results[env] = env_results
    # Make plots.
    _generate_plots(results, plot_filepath)


def _run_single_env(
    env: str,
    seeds: Set[int],
    timeout: int = TIMEOUT,
) -> Tuple[List[int], Dict[str, List[List[List[float]]]]]:
    env_xs: Optional[List[int]] = None
    approach_to_env_ys: Dict[str, List[List[List[float]]]] = {
        "chatgpt4": [],
        "fd-lama-first": [],
    }
    for i, seed in enumerate(sorted(seeds)):
        print(f"STARTING SEED {seed} ({i} out of {len(seeds)})")
        # Load the genplan for this seed.
        genplan = _load_genplan(env, seed)
        # Generate and evaluate on problems.
        for env_ys in approach_to_env_ys.values():
            env_ys.append([])
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
                        plan, metrics = utils.run_fastdownward_planning(
                            task, timeout=timeout
                        )
                        duration = metrics["duration"]
                    # Validate the plan.
                    success, _ = utils.validate_plan(task, plan)
                    if not success:
                        print("WARNING: plan invalid.")
                        duration = float(timeout)
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
        all_num_items = [1, 4, 16, 64, 256]
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
    # Gripper
    elif env == "pg3-manygripper":
        np.random.seed(seed)
        all_multipliers = [1, 2, 8, 32, 128]
        domain_filepath = utils.PDDL_DIR / "pg3" / "manygripper.pddl"
        with open(domain_filepath, "r", encoding="utf-8") as f:
            domain_str = f.read()
        domain = PDDLDomainParser(
            domain_filepath, expect_action_preds=False, operators_as_actions=True
        )
        with tempfile.TemporaryDirectory() as td:
            problem_dir = Path(td)
            for multiplier in all_multipliers:
                num_balls = multiplier
                num_rooms = 2 * multiplier
                num_objs: Optional[int] = None
                tasks = []
                for i in range(num_tasks_per_size):
                    problem_outfile = f"problem{i}.pddl"
                    gripper_gen(
                        domain,
                        problem_dir,
                        problem_outfile,
                        min_num_balls=num_balls,
                        max_num_balls=num_balls,
                        min_num_rooms=num_rooms,
                        max_num_rooms=num_rooms,
                        min_num_balls_goal=num_balls,
                        max_num_balls_goal=num_balls,
                    )
                    pddl_outfile = problem_dir / problem_outfile
                    with open(pddl_outfile, "r", encoding="utf-8") as f:
                        problem_str = f.read()
                    task = Task(domain_str, problem_str)
                    if num_objs is None:
                        num_objs = len(task.objects)
                    assert num_objs == len(task.objects)
                    tasks.append(task)
                assert num_objs is not None
                assert len(tasks) == num_tasks_per_size
                yield (num_objs, tasks)
    # Ferry
    elif env == "pg3-manyferry":
        random.seed(seed)
        all_multipliers = [1, 2, 8, 32, 128]
        domain_filepath = utils.PDDL_DIR / "pg3" / "manyferry.pddl"
        with open(domain_filepath, "r", encoding="utf-8") as f:
            domain_str = f.read()
        for multiplier in all_multipliers:
            num_locs = 2 * multiplier
            num_cars = multiplier
            num_objs = None
            tasks = []
            for i in range(num_tasks_per_size):
                problem_str = ferry_gen(num_locs, num_cars)
                task = Task(domain_str, problem_str)
                if num_objs is None:
                    num_objs = len(task.objects)
                assert num_objs == len(task.objects)
                tasks.append(task)
            assert num_objs is not None
            assert len(tasks) == num_tasks_per_size
            yield (num_objs, tasks)
    # Hiking
    elif env == "pg3-hiking":
        np.random.seed(seed)
        all_grid_sizes = [4, 8, 16, 24, 32]
        domain_filepath = utils.PDDL_DIR / "pg3" / "hiking.pddl"
        with open(domain_filepath, "r", encoding="utf-8") as f:
            domain_str = f.read()
        domain = PDDLDomainParser(
            domain_filepath, expect_action_preds=False, operators_as_actions=True
        )
        with tempfile.TemporaryDirectory() as td:
            problem_dir = Path(td)
            for grid_size in all_grid_sizes:
                num_objs = None
                tasks = []
                for i in range(num_tasks_per_size):
                    problem_outfile = f"problem{i}.pddl"
                    grid = np.array(generate_random_grid(grid_size, grid_size))
                    hiking_gen(grid, domain, problem_dir, problem_outfile)
                    pddl_outfile = problem_dir / problem_outfile
                    with open(pddl_outfile, "r", encoding="utf-8") as f:
                        problem_str = f.read()
                    task = Task(domain_str, problem_str)
                    if num_objs is None:
                        num_objs = len(task.objects)
                    assert num_objs == len(task.objects)
                    tasks.append(task)
                assert num_objs is not None
                assert len(tasks) == num_tasks_per_size
                yield (num_objs, tasks)
    # Newspapers
    elif env == "pg3-trapnewspapers":
        np.random.seed(seed)
        all_multipliers = [1, 2, 8, 32, 128]
        domain_filepath = utils.PDDL_DIR / "pg3" / "trapnewspapers.pddl"
        with open(domain_filepath, "r", encoding="utf-8") as f:
            domain_str = f.read()
        domain = PDDLDomainParser(
            domain_filepath, expect_action_preds=False, operators_as_actions=True
        )
        with tempfile.TemporaryDirectory() as td:
            problem_dir = Path(td)
            for multiplier in all_multipliers:
                num_locs = 2 * multiplier
                num_newspapers = 3 * multiplier
                num_want_locs = multiplier
                num_objs = None
                tasks = []
                for i in range(num_tasks_per_size):
                    problem_outfile = f"problem{i}.pddl"
                    news_gen(
                        domain,
                        problem_dir,
                        problem_outfile,
                        num_locs,
                        num_want_locs,
                        num_newspapers,
                    )
                    pddl_outfile = problem_dir / problem_outfile
                    with open(pddl_outfile, "r", encoding="utf-8") as f:
                        problem_str = f.read()
                    task = Task(domain_str, problem_str)
                    if num_objs is None:
                        num_objs = len(task.objects)
                    assert num_objs == len(task.objects)
                    tasks.append(task)
                assert num_objs is not None
                assert len(tasks) == num_tasks_per_size
                yield (num_objs, tasks)
    else:
        raise NotImplementedError(f"Unrecognized environment: {env}")


def _generate_plots(
    results: Dict[str, Tuple[List[int], Dict[str, List[List[List[float]]]]]],
    outfile_path: Path,
) -> None:
    num_subplots = len(results)
    with plt.style.context("bmh"):
        fig, _ = plt.subplots(
            1, num_subplots, figsize=(5 * num_subplots, 7), sharey=True
        )
        ax = None
        for i, (ax, env) in enumerate(zip(fig.axes, ENV_ORDER)):
            env_xs, approach_to_env_ys = results[env]
            for approach in sorted(approach_to_env_ys):
                env_ys = approach_to_env_ys[approach]  # (seeds, objects, tasks)
                median_env_ys = np.median(env_ys, axis=(0, 2))
                assert len(env_xs) == len(median_env_ys)
                ax.loglog(
                    env_xs,
                    median_env_ys,
                    marker="o",
                    label=APPROACH_TO_LABEL[approach],
                    linewidth=5,
                    markersize=12,
                )
            ax.loglog(
                [-100, 10 * max(env_xs)],
                [TIMEOUT, TIMEOUT],
                linestyle="--",
                linewidth=5,
                markersize=12,
                label="Timeout",
            )
            ax.set_xlim(right=1.25 * max(env_xs))
            if i == 0:
                ax.set_yticks([1e-3, 1e-2, 1e-1, 1e0, 10, 100])
            ax.set_title(ENV_TO_LABEL[env], fontsize=48)
            ax.set_xticks([10, 100])
        assert ax is not None
        fig.supxlabel("# Objects", fontsize=36)
        fig.supylabel("Planning Time (s)", x=0.01, fontsize=36)
        plt.tight_layout()
        plt.savefig(outfile_path, dpi=500)
        # Save legend as separate figure.
        legend_fig = plt.figure()
        legend = legend_fig.legend(
            *ax.get_legend_handles_labels(), framealpha=1, frameon=False
        )
        bbox = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        legend_outfile_path = outfile_path.parent / f"legend-{outfile_path.name}"
        bbox_extents = bbox.extents
        bbox_extents[:2] -= 0.1
        bbox_extents[2:] += 0.1
        bbox = bbox.from_extents(bbox_extents)
        plt.savefig(legend_outfile_path, dpi=500, bbox_inches=bbox)
    print(f"Wrote out to {outfile_path}")
    print(f"Wrote out to {legend_outfile_path}")


if __name__ == "__main__":
    _main()
