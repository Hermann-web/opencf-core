#!/bin/bash

DOCS_DIR=$(realpath ./docs)
POETRY_DIR=$(realpath ./docs)
PROJECT_DIR=$(realpath .)

# starting point
HERE=$PWD
cd $POETRY_DIR

# create a new pyproject.toml file, using python>=3.8.1 and buildthedocs requirements
echo "-> setting up env data ..."
## add buildthedocs requirements to main file # sphinx needs old requirements to work
cat $PROJECT_DIR/pyproject.toml $POETRY_DIR/pyproject.part.toml > $POETRY_DIR/pyproject.toml
## use python3.8.1 instead of 3.7
sed -i 's/^python =.*/python = "\^3\.8\.1"/' "$POETRY_DIR/pyproject.toml"
## Replace "name =" with "name = \"buildthedocs\""
sed -i 's/^name =.*/name = "buildthedocs"/' "$POETRY_DIR/pyproject.toml"

# clean old env and install new one and save requirements
echo "-> cleaning env ..."
rm poetry.lock
rm -rf $(poetry env info --path)
poetry install --no-root
poetry export -f requirements.txt --output $DOCS_DIR/requirements.txt --without-hashes --with buildthedocs

# setup docs files and activate env
echo "-> setup docs files ..."
poetry run sphinx-apidoc $PROJECT_DIR/convcore/ -o $DOCS_DIR/source/convcore/ -f -E
PYTHON_PATH="$(poetry env info --path)"
source "$PYTHON_PATH/bin/activate"

# build docs
echo "-> building docs ..."
cd $DOCS_DIR
rm -r build
make html

# deactivate and remove env
echo "-> removing env ..."
deactivate 
rm -rf $PYTHON_PATH
rm pyproject.toml
rm poetry.lock

# final point
cd $HERE
open $DOCS_DIR/build/html/index.html
