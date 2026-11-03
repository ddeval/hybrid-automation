#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

my_path="$HOME/hybrid-automation"

for folder in Jenkinsfiles network-automation docker ansible terraform .github/workflows; do
    mkdir -p "$my_path/$folder"
done