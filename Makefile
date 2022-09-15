install:
		pip install --upgrade pip && pip install -r requirements.txt

format:
		black *.py helpers/*.py
lint:
		pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py window.py   helpers/logic.py
test:
		python -m pytest -vv --cov=helpers test_logic.py
build:
		#container building
deploy:

all: install lint test deploy




