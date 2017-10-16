.DEFAULT_GOAL := help

# AutoEnv
ENV ?= .env
ENV_GEN := $(shell ./.env.gen ${ENV} .env.required)
include ${ENV}
export $(shell sed 's/=.*//' ${ENV})


# AutoDoc
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: deps
deps:
	pip install -U -r requirements.txt

.PHONY: install
install:
	make deps
	rm -rf dist/*
	python setup.py sdist
	pip install -U dist/*

.PHONY: upload-pypi
upload-pypi:
	pip install --upgrade pip setuptools wheel
	pip install twine
	sh pypi_upload.sh