#!/bin/bash
mypy .
pytest . --pylint -m pylint --pylint-rcfile=.llm_genplan_pylintrc
./run_autoformat.sh
pytest tests/
