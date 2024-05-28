MODULE=./opencf_core
TEST_MODULE=./tests

echo "-> running isort ..."
poetry run isort $MODULE $TEST_MODULE

echo "-> running black ..."
poetry run black $MODULE $TEST_MODULE

# echo "-> running pylint ..."
# pylint $MODULE

echo "-> running mypy..."
poetry run mypy $MODULE $TEST_MODULE 

echo "-> running flake8 ..."
poetry run flake8 $MODULE $TEST_MODULE 
