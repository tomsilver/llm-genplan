# Generalized Planning with Large Language Models

![workflow](https://github.com/tomsilver/llm-genplan/actions/workflows/ci.yml/badge.svg)

Under development.

## Requirements

- Python 3.11+
- Tested on MacOS Catalina

## Installation

1. Recommended: create and source a virtualenv.
2. `pip install -e ".[develop]"`

## Check Installation

Run `./run_ci_checks.sh`. It should complete with all green successes in 5-10 seconds.

## Usage

1. Open [chat.openai.com](https://chat.openai.com/) in your web browser.
2. Run a command like the example below and follow the instructions in the terminal. **Note that your copy-paste clipboard will be automatically updated.**

Example command:

```python llm_genplan/main.py --env pg3-manygripper --seed 0 --experiment_id chatgpt4 --num_prompt_tasks 2 --num_extra_train_tasks 8 --num_eval_tasks 30 --abbreviate_problem_strs```