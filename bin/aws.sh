#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
DIR="$(readlink -f "$DIR")"
sam local start-api --template "$DIR/backend/template.yaml"
