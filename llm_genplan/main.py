"""Main entry point for experiments.

Example commands:
    python llm_genplan/main.py --env pyperplan-blocks --seed 0 \
        --experiment_id test
"""

import logging
import os
import sys
import time

from llm_genplan import utils
from llm_genplan.envs import create_tasks
from llm_genplan.flags import FLAGS, parse_flags
from llm_genplan.genplan import get_genplan_from_llm


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
    train_tasks, eval_tasks = create_tasks(
        env_name=FLAGS.env,
        num_train=FLAGS.num_train_tasks,
        num_eval=FLAGS.num_eval_tasks,
    )

    # Go back and forth with ChatGPT until it finds a generalized plan that
    # works on all of the train tasks, or until we run out of patience.
    logging.info("Starting conversation with LLM.")
    save_path = utils.CACHE_DIR / f"{FLAGS.env}_{FLAGS.seed}_{FLAGS.experiment_id}"
    os.makedirs(save_path, exist_ok=True)
    generalized_plan = get_genplan_from_llm(
        train_tasks, save_path, horizon=FLAGS.horizon, timeout=FLAGS.timeout
    )

    # Evaluate the generalized plan on the held-out evaluation tasks.
    num_successes = 0
    num_eval = len(eval_tasks)
    for i, eval_task in enumerate(eval_tasks):
        success, info = utils.run_genplan_on_task(
            generalized_plan, eval_task, horizon=FLAGS.horizon, timeout=FLAGS.timeout
        )
        success_str = "Solved" if success else "Failed"
        logging.info(f"Eval task {i+1}/{num_eval}: {success_str} [{info}]")
        if success:
            num_successes += 1
    logging.info(
        f"Generalized plan solved {num_successes}/{num_eval} "
        "held-out evaluation tasks."
    )

    script_time = time.time() - script_start
    logging.info(f"\n\nMain script terminated in {script_time:.5f} seconds")


if __name__ == "__main__":  # pragma: no cover
    _main()
