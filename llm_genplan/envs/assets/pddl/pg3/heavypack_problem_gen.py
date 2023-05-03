"""Generate problems for the heavy-pack domain."""

from pathlib import Path
from typing import List

import numpy as np

from llm_genplan.utils import PDDL_DIR


def _generate_problem_str(
    min_num_items: int,
    max_num_items: int,
    rng: np.random.Generator,
    min_obj_id: int = 0,
    max_obj_id: int = 1000,
) -> str:
    num_items = rng.integers(min_num_items, max_num_items + 1)
    objs = {f"o{rng.integers(min_obj_id, max_obj_id+1)}" for _ in range(num_items)}
    objs_str = " ".join(sorted(objs))
    unpacked_str = "\n    ".join(f"(unpacked {o})" for o in sorted(objs))
    goal_packed_str = " ".join(f"(packed {o})" for o in sorted(objs))
    objs_by_weight = sorted(objs)
    rng.shuffle(objs_by_weight)
    heavier_strs: List[str] = []
    for i, o in enumerate(objs_by_weight):
        for other in objs_by_weight[i + 1 :]:
            heavier_strs.append(f"(heavier {o} {other})")
    heavier_str = "\n    ".join(heavier_strs)

    return f"""(define (problem heavy-pack-prob)
	(:domain heavy-pack)
	(:objects {objs_str})

(:init
    (box-empty)
    {unpacked_str}
    {heavier_str}
)

(:goal (and {goal_packed_str}))
)
"""


def _run(
    train_dir: Path,
    test_dir: Path,
    num_seed: int,
    num_train_per_seed: int,
    num_test_per_seed: int,
    train_min_num_items: int = 3,
    train_max_num_items: int = 10,
    test_min_num_items: int = 100,
    test_max_num_items: int = 250,
    seed_offset: int = 0,
) -> None:
    for seed in range(num_seed):
        rng = np.random.default_rng(seed + seed_offset)
        train_seed_dir = train_dir / f"seed{seed + seed_offset}"
        train_seed_dir.mkdir(parents=True, exist_ok=True)
        test_seed_dir = test_dir / f"seed{seed + seed_offset}"
        test_seed_dir.mkdir(parents=True, exist_ok=True)

        # Generate train problems.
        for task_idx in range(num_train_per_seed):
            problem_str = _generate_problem_str(
                train_min_num_items, train_max_num_items, rng
            )
            filepath = train_seed_dir / f"task{task_idx}.pddl"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(problem_str)
            print(f"Wrote out problem to {filepath}.")

        # Generate test problems.
        for task_idx in range(num_test_per_seed):
            problem_str = _generate_problem_str(
                test_min_num_items, test_max_num_items, rng
            )
            filepath = test_seed_dir / f"task{task_idx}.pddl"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(problem_str)
            print(f"Wrote out problem to {filepath}.")


if __name__ == "__main__":
    _run(
        PDDL_DIR / "pg3" / "heavypack",
        PDDL_DIR / "pg3" / "heavypack_test",
        num_seed=10,
        num_train_per_seed=10,
        num_test_per_seed=30,
    )
