install:
		pip install --upgrade pip && pip install -r requirements.txt

format:
		black *.py helpers/*.py
lint:
		pylint --disable=R,C main.py
test:
		python -m pytest -vv main-test.py
deploy:

all: install lint test deploy




