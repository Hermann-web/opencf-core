MODULE=./opencf_core
TEST_MODULE=./tests
EXAMPLES_MODULE=./examples

echo "-> running prettier on both readme ..."
prettier README.md examples/readme.md -w

echo "-> running isort ..."
poetry run isort $MODULE $TEST_MODULE $EXAMPLES_MODULE/*.py

echo "-> running black ..."
poetry run black $MODULE $TEST_MODULE $EXAMPLES_MODULE/*.py

echo "-> running pylint ..."
pylint $MODULE $TEST_MODULE $EXAMPLES_MODULE/*.py

echo "-> running mypy..."
poetry run mypy $MODULE $TEST_MODULE $EXAMPLES_MODULE/*.py

echo "-> running flake8 ..."
poetry run flake8 $MODULE $TEST_MODULE $EXAMPLES_MODULE/*.py
