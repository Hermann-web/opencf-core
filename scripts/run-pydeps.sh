#!/bin/bash

# Set the target directory
TARGET_DIR="./opencf_core/"
OUTPUT_DIR="./docs/"

echo "-> running pydoc-markdown ..."
pydoc-markdown -I . --render-toc --site-dir out --build > ${OUTPUT_DIR}index.md

echo "-> running pydeps ..."
pydeps $TARGET_DIR --cluster --rankdir LR --max-module-depth=3 -o ${OUTPUT_DIR}deps-d3.svg --noshow
