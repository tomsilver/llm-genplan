#!/bin/bash

# Script to create ablated versions of all PDDL domains and tasks.
# Run from top-level directory.

set -e  # exit on error

for SEED in {0..9}
do
    python scripts/pddl_replace.py --env pg3-manygripper --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30
    python scripts/pddl_replace.py --env pg3-manyferry --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30
    python scripts/pddl_replace.py --env pg3-manymiconic --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30
    python scripts/pddl_replace.py --env pg3-spannerlearning --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30
    python scripts/pddl_replace.py --env pg3-hiking --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 2 --num_eval_tasks 30
    python scripts/pddl_replace.py --env pg3-trapnewspapers --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 3 --num_eval_tasks 30
    python scripts/pddl_replace.py --env pg3-heavypack --seed $SEED --experiment_id not-used --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30
done
