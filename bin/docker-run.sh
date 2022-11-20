#!/usr/bin/env bash
# This is run automatically by the docker container.
set -euo pipefail
IFS=$'\n\t'

pip install -r frontend/requirements.txt
python frontend/manage.py runserver "0.0.0.0:8000"
