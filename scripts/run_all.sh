# Script to reproduce all results, assuming responses from GPT are cached.

for SEED in {1..9}
do
    # Main approach.
    python llm_genplan/main.py --env pg3-manygripper --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --env pg3-manyferry --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --env pg3-manymiconic --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --env pg3-spannerlearning --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --env pg3-hiking --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 2 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --env pg3-trapnewspapers --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 3 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache

    # Ablate interactive debugging.
    python llm_genplan/main.py --experiment_id chatgpt4-no-debug --load_experiment_id chatgpt4 --max_debug_attempts 0 --env pg3-manygripper --seed $SEED --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --experiment_id chatgpt4-no-debug --load_experiment_id chatgpt4 --max_debug_attempts 0 --env pg3-manyferry --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --experiment_id chatgpt4-no-debug --load_experiment_id chatgpt4 --max_debug_attempts 0 --env pg3-manymiconic --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --experiment_id chatgpt4-no-debug --load_experiment_id chatgpt4 --max_debug_attempts 0 --env pg3-spannerlearning --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --experiment_id chatgpt4-no-debug --load_experiment_id chatgpt4 --max_debug_attempts 0 --env pg3-hiking --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 2 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache
    python llm_genplan/main.py --experiment_id chatgpt4-no-debug --load_experiment_id chatgpt4 --max_debug_attempts 0 --env pg3-trapnewspapers --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 3 --num_eval_tasks 30 --abbreviate_problem_strs --force_load_from_cache

done
