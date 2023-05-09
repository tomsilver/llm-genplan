# Generalized Planning in PDDL Domains with Pretrained Large Language Models

![workflow](https://github.com/tomsilver/llm-genplan/actions/workflows/ci.yml/badge.svg)

Preprint coming soon.

## Requirements

- Python 3.11+
- Tested on MacOS Catalina

## Installation

1. Recommended: create and source a virtualenv.
2. `pip install -e ".[develop]"`

## Check Installation

Run `./run_ci_checks.sh`. It should complete with all green successes in 5-10 seconds.

## Reproduce Results

Run `./scripts/run_all.sh`. This reproduces results using cached chat logs. It will take 12-16 hours to complete.

## Examine Chat Logs

See `llm_genplan/llm_cache`.
