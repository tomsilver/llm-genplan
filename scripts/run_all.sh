# Script to reproduce all results, assuming responses from GPT are cached.

for SEED in {0..9}
do
    python llm_genplan/main.py --env pg3-manygripper --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs
    python llm_genplan/main.py --env pg3-manyferry --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs
    python llm_genplan/main.py --env pg3-manymiconic --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs
    python llm_genplan/main.py --env pg3-spannerlearning --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs
    python llm_genplan/main.py --env pg3-hiking --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 2 --num_eval_tasks 30 --abbreviate_problem_strs
    python llm_genplan/main.py --env pg3-trapnewspapers --seed $SEED --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 3 --num_eval_tasks 30 --abbreviate_problem_strs
done
