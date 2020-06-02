setup:
	mkdir local_environment
	cd local_environment
    python3 -m venv venv
	source venv/bin/activate

install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    python -m pytest -vv --cov=myrepolib tests/*.py
    python -m pytest --nbval notebook.ipynb


lint:
    pylint --disable=R,C myrepolib cli web

all: install lint test