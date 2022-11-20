#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
DIR="$(readlink -f "$DIR")"
# Windows
# MacOS
# Linux
if ! python3 --version ; then
  echo "python3 is not installed"
  exit 1
  else
  if python3 -c """
import sys
if sys.base_prefix == sys.prefix:
  print('Please activate a python virtual environment before installing dependencies.')
  sys.exit(1)
else:
  print('Virtual environment is install at' + sys.prefix)
  """ ; then
    echo "Continuing"
  else
    echo "Attempting to install a python virtual environment to ${DIR}/venv"
    python3 -m venv venv
    source venv/bin/activate
  fi
    pip install -r frontend/requirements.txt
    python3 frontend/manage.py runserver "0.0.0.0:8000"
fi

