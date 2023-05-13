"""Utilities."""

import functools
import logging
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from llm_genplan.flags import FLAGS, create_parser
from llm_genplan.structs import Metrics, Task

# Global constants.
_DIR = Path(__file__).parent
PDDL_DIR = _DIR / "envs" / "assets" / "pddl"
CACHE_DIR = _DIR / "llm_cache"


@functools.lru_cache(maxsize=None)
def get_git_commit_hash() -> str:
    """Return the hash of the current git commit."""
    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"])
    except subprocess.CalledProcessError:
        logging.warning("Code is not inside a git repository.")
        return "not-a-git-repository"
    return out.decode("ascii").strip()


def get_config_path_str() -> str:
    """Get a string identifier for an experiment from FLAGS."""
    return f"{FLAGS.env}__{FLAGS.seed}__{FLAGS.experiment_id}"


def get_pddl_from_url(url: str, cache_dir: Path = PDDL_DIR) -> str:
    """Download a PDDL file from a given URL.

    If the file already exists in the cache_dir, load instead.

    Note that this assumes the PDDL won't change at the URL.
    """
    sanitized_url = "".join(x for x in url if x.isalnum())
    file_name = f"cached-pddl-{sanitized_url}"
    file_path = cache_dir / file_name
    # Download if doesn't already exist.
    if not os.path.exists(file_path):
        logging.info(f"Cache not found for {url}, downloading.")
        try:
            with urllib.request.urlopen(url) as f:
                pddl = f.read().decode("utf-8").lower()
        except urllib.error.HTTPError:
            raise ValueError(f"PDDL file not found at {url}.")
        if "(:action" not in pddl and "(:init" not in pddl:
            raise ValueError(f"PDDL file not found at {url}.")
        # Cache.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(pddl)
    with open(file_path, "r", encoding="utf-8") as f:
        pddl = f.read()
    return pddl


def validate_plan(task: Task, plan: List[str]) -> Tuple[bool, str]:
    """Use VAL to check if a plan solves a PDDL problem."""
    plan_str = ""
    for t, action in enumerate(plan):
        plan_str += f"{t}: {action}\n"
    plan_file = tempfile.NamedTemporaryFile(delete=False).name
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write(plan_str)
    val_dir = Path(__file__).parent / "third_party" / "val"
    if sys.platform == "darwin":  # pragma: no cover
        platform_dir = "darwin"
    else:  # pragma: no cover
        assert sys.platform.startswith("linux")
        platform_dir = "linux64"
    val = val_dir / platform_dir / "Validate"
    cmd_str = f'"{val}" -v "{task.domain_file}" "{task.problem_file}" ' f'"{plan_file}"'
    output = subprocess.getoutput(cmd_str)
    os.remove(plan_file)
    if "Plan valid" in output:
        return True, "Plan succeeded."
    repair_phrase = "Plan Repair Advice:"
    if repair_phrase in output:
        msg = output[output.index(repair_phrase) + len(repair_phrase) :]
        msg, _ = msg.split("Failed plans:")
        msg = "NOTE: " + msg.strip()
    else:
        msg = "NOTE: The plan did not achieve the goal."
    return False, msg


def set_to_reproducible_str(s: Set) -> str:
    """Create a string representation for a set deterministically."""
    return "{" + ", ".join(map(repr, sorted(s))) + "}"


def reset_flags(args: Optional[Dict[str, Any]] = None, default_seed: int = 123) -> None:
    """Reset FLAGS for tests."""
    parser = create_parser()
    default_args = parser.parse_args(
        [
            "--env",
            "default env placeholder",
            "--seed",
            str(default_seed),
            "--experiment_id",
            "default experiment_id placeholder",
        ]
    )
    arg_dict = default_args.__dict__.copy()
    if args is not None:
        arg_dict.update(args)
    FLAGS.__dict__.update(arg_dict)


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
        duration = float(timeout)
    else:
        total_time = re.findall(r"Total time: (\d+\.\d+)", output)[0]
        duration = float(total_time)
    metrics = {
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
