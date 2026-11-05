#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

my_path="$HOME/hybrid-automation"

for folder in  network-automation docker ansible terraform .github/workflows; do
    mkdir -p "$my_path/$folder/"
done

for folder in  network-automation docker ansible terraform .github/workflows; do
    touch "$my_path/$folder/.gitkeep"
done