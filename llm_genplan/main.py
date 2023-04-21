"""Main entry point for experiments.

Example commands:     python llm_genplan/main.py --env pyperplan-gripper
--seed 0 --experiment_id chatgpt4
"""

import logging
import os
import pickle
import sys
import time
from pathlib import Path

from llm_genplan import utils
from llm_genplan.envs import create_tasks
from llm_genplan.flags import FLAGS, parse_flags
from llm_genplan.genplan import get_genplan_from_llm, run_genplan_on_task
from llm_genplan.structs import Metrics, TaskMetrics


def _main() -> None:
    # Basic setup.
    script_start = time.time()
    str_args = " ".join(sys.argv)
    # Parse command-line flags.
    parse_flags()
    # Set up logging.
    logging.basicConfig(
        level=FLAGS.loglevel, format="%(message)s", handlers=[logging.StreamHandler()]
    )
    logging.info(f"Running command: python {str_args}")
    logging.info("Full config:")
    logging.info(FLAGS)
    logging.info(f"Git commit hash: {utils.get_git_commit_hash()}")

    # Generate train and eval tasks.
    logging.info("Generating tasks.")
    prompt_tasks, extra_train_tasks, eval_tasks = create_tasks(
        env_name=FLAGS.env,
        num_prompt=FLAGS.num_prompt_tasks,
        num_train=FLAGS.num_extra_train_tasks,
        num_eval=FLAGS.num_eval_tasks,
    )

    # Go back and forth with ChatGPT until it finds a generalized plan that
    # works on all of the train tasks, or until we run out of patience.
    logging.info("Starting conversation with LLM.")
    save_path = utils.CACHE_DIR / f"{FLAGS.env}_{FLAGS.seed}_{FLAGS.experiment_id}"
    os.makedirs(save_path, exist_ok=True)
    generalized_plan = get_genplan_from_llm(
        prompt_tasks,
        extra_train_tasks,
        save_path,
        horizon=FLAGS.horizon,
        timeout=FLAGS.timeout,
    )

    # Evaluate the generalized plan on the held-out evaluation tasks.
    results: Metrics = {}
    num_successes = 0
    num_eval = len(eval_tasks)
    for i, eval_task in enumerate(eval_tasks):
        task_id = f"{eval_task.domain_name}_seed{FLAGS.seed}_problem{i}"
        task_metrics: TaskMetrics = {}
        results[task_id] = task_metrics
        success, info = run_genplan_on_task(
            generalized_plan, eval_task, horizon=FLAGS.horizon, timeout=FLAGS.timeout
        )
        success_str = "Solved" if success else "Failed"
        logging.info(f"Eval task {i+1}/{num_eval}: {success_str} [{info}]")
        if success:
            num_successes += 1
        task_metrics["success"] = success
    logging.info(
        f"Generalized plan solved {num_successes}/{num_eval} "
        "held-out evaluation tasks."
    )

    # Save the results.
    os.makedirs(FLAGS.results_dir, exist_ok=True)
    outdata = {
        "config": FLAGS,
        "results": results.copy(),
        "git_commit_hash": utils.get_git_commit_hash(),
    }
    outfile = Path(FLAGS.results_dir) / f"{utils.get_config_path_str()}.pkl"
    with open(outfile, "wb") as f:
        pickle.dump(outdata, f)

    script_time = time.time() - script_start
    logging.info(f"\n\nMain script terminated in {script_time:.5f} seconds")


if __name__ == "__main__":  # pragma: no cover
    _main()
