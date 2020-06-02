#!/bin/bash
setup:
	mkdir local_environment
	cd local_environment
    python3 -m venv venv
	source venv/bin/activate

install:
    pip3 install --upgrade pip &&\
        pip3 install -r requirements.txt

test:
    python -m pytest -vv --cov=myrepolib tests/*.py
    python -m pytest --nbval notebook.ipynb

validate-circleci:
    # See https://circleci.com/docs/2.0/local-cli/#processing-a-config
    circleci config process .circleci/config.yml

run-circleci-local:
    # See https://circleci.com/docs/2.0/local-cli/#running-a-job
    circleci local execute

lint:
    # Lint Dockerfile
    hadolint demos/flask-sklearn/Dockerfile
    # Lint python files
    pylint --disable=R,C myrepolib cli web

all: install lint test