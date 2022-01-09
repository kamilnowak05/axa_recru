SHELL=/bin/bash

RUN_SERVER_FILE=fill_server.py
VENV_NAME=venv
VENV_BIN=$(shell pwd)/${VENV_NAME}/bin
PYTHON=${VENV_BIN}/python3


.DEFAULT_GOAL := help

help:
	@echo "Available Makefile targets:"
	@echo "* venv"
	@echo "    Create virtualenv and install dependencies"
	@echo "* run"
	@echo "    Start server"


venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: requirements.txt
	@echo "***** Checking virtualenv..."
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	@echo "***** Updating pip..."
	${PYTHON} -m pip install -U pip
	@echo "***** Updating dependencies..."
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate

run: venv
	${PYTHON} $(RUN_SERVER_FILE)