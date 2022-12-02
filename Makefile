default: help

help:
	@echo "Comandos - Banco Imobiliario"
	@echo "Ajuda"
	@echo
	@echo  "uso: make <sub comando>"
	@echo  "Sub comandos:"
	@echo  "    run""					        ""Rodar projeto"
	@echo  "    run_test""					""Rodar teste de cobertura de codigo e pytest com modular fixture"

VENV = venv
PYTHON = $(VENV)/bin/python3.10
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) src/main.py


$(VENV)/bin/activate: requirements.txt
	 python3 -m venv $(VENV)
	 $(PIP) install -r requirements.txt


clean:
	rm -rf __pycache__
	rm -rf $(VENV)