.PHONY: run lint test
.DEFAULT_GOAL := install

manage-%: venv
	@. venv/bin/activate && cd src && python manage.py $*

guard-%:
	@if [ "${${*}}" == "" ]; then echo -e "\nERROR: variable $* not set\n" && exit 1; fi

venv: 
	@virtualenv -p /usr/bin/python3 venv

install: venv
	@. venv/bin/activate && pip install -r deploy/requirements/development.txt

run: \
	manage-syncdb
	@. venv/bin/activate && cd src && python manage.py runserver 0.0.0.0:8000

lint:
	@# simple writing quality to ensure a common idiom for everyone
	@flake8 src
	@# ignore paths in .jshintignore
	@jshint --verbose src

test:
	@# unit tests
	@cd src && python manage.py test
	@# karma start --single-run  --reporter dot

