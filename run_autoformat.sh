#!/bin/bash
python -m black .
docformatter -i -r . --exclude venv
isort .
