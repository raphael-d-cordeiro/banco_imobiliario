default: help

help:
	@echo "Comandos - Banco Imobiliario"
	@echo "Ajuda"
	@echo
	@echo  "uso: make <sub comando>"
	@echo  "Sub comandos:"
	@echo  "    dependencies""					""Criar venv e instalar as deps Python"
	@echo  "    run""							""Rodar projeto"
	@echo  "    run_test""						""Rodar teste de cobertura de codigo e pytest com modular fixture"

VENV = venv
PYTHON = $(VENV)/bin/python3.10
PIP = $(VENV)/bin/pip

.PHONY: run clean

dependencies: requirements.txt
	 python3.10 -m venv $(VENV)
	 $(PIP) install --upgrade pip
	 $(PIP) install -r requirements.txt

run:
	$(PYTHON) src/main.py

run_test:
	$(VENV)/bin/pytest --cov-append --cov=src src/tests/

clean:
	rm -rf __pycache__
	rm -rf $(VENV)