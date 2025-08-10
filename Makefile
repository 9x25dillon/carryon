.ONESHELL:
VENV?=.venv
PY?=$(VENV)/bin/python
PIP?=$(VENV)/bin/pip

install:
	python3 -m venv $(VENV)
	$(PIP) install -U pip
	$(PIP) install -e server

dev:
	$(VENV)/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --app-dir server

test:
	PYTHONPATH=server $(VENV)/bin/pytest -q server

fmt:
	$(VENV)/bin/black server/app

lint:
	$(VENV)/bin/ruff check server/app