"""Utilities."""

import functools
import logging
import os
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path
from typing import List, Set, Tuple

from llm_genplan.structs import Task

# Global constants.
_DIR = Path(__file__).parent
PDDL_DIR = _DIR / "envs" / "assets" / "pddl"
CACHE_DIR = _DIR / "llm_cache"


@functools.lru_cache(maxsize=None)
def get_git_commit_hash() -> str:
    """Return the hash of the current git commit."""
    out = subprocess.check_output(["git", "rev-parse", "HEAD"])
    return out.decode("ascii").strip()


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
        msg = msg.strip()
    else:
        msg = "The plan did not achieve the goal."
    return False, msg


def set_to_reproducible_str(s: Set) -> str:
    """Create a string representation for a set deterministically."""
    return "{" + ", ".join(map(repr, sorted(s))) + "}"
