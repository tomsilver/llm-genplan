"""Command line flags."""

import argparse
import logging

FLAGS = argparse.Namespace()  # set by parse_flags() below


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser.

    Separated out for testing.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", required=True, type=str)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--experiment_id", required=True, type=str)
    parser.add_argument("--num_prompt_tasks", default=2, type=int)
    parser.add_argument("--num_extra_train_tasks", default=5, type=int)
    parser.add_argument("--num_eval_tasks", default=10, type=int)
    parser.add_argument("--horizon", default=1000000, type=int)
    parser.add_argument("--timeout", default=30, type=int)
    parser.add_argument("--exclude_inputs_in_feedback", action="store_true")
    parser.add_argument("--prompt_problem_distribution", default="none", type=str)
    parser.add_argument(
        "--debug",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    return parser


def parse_flags() -> None:
    """Parse the command line flags and update global FLAGS."""
    parser = create_parser()
    args = parser.parse_args()
    FLAGS.__dict__.update(args.__dict__)
