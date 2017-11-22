settings=championship.settings
manage=python championship/manage.py


all: help

# comandos para ejecutar en local
run:
	$(manage) runserver $(p) --settings=$(settings).local

collectstatic:
	$(manage) collectstatic --noinput --settings=$(settings).local
	

cleanpycs:
	@echo "Limpiando archivos .pyc del proyecto"
	@find . -name '*.pyc' -delete
	@echo "Archivos pyc eliminados"

shell:
	$(manage) shell --settings=$(settings).local

	
makemigrations:
	$(manage) makemigrations $(mod) --settings=$(settings).local

migrate:
	$(manage) migrate $(mod) $(v) --settings=$(settings).local

createsuperuser:
	$(manage) createsuperuser --settings=$(settings).local
	
requisitos:
	pip install -r requisitos.txt

setperfiles:
	$(manage) setperfiles --verbose 1 --settings=$(settings).local

dump_initial:
	$(manage) dumpdata --natural-foreign --natural-primary --indent 4 --settings=$(settings).local > docs/data_inicial.json

load_initial:
	@echo "Cargando los datos iniciales"
	@$(manage) loaddata docs/data_inicial.json --settings=$(settings).local

