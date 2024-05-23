MODULE=./opencf_core

echo "-> running isort ..."
poetry run isort $MODULE

echo "-> running black ..."
poetry run black $MODULE

# echo "-> running pylint ..."
# pylint $MODULE

echo "-> running mypy..."
poetry run mypy $MODULE 

echo "-> running flake8 ..."
poetry run flake8 $MODULE
