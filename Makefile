# TODO Update this variable
MODULE := hello_world

##@ General

.PHONY: help
help:  ## Show rules help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: all
all: format lint doc test

.PHONY: deps
deps: .venv  ## Install dependencies in a python virtual environment
	source .venv/bin/activate; python3 -m poetry install --no-root
	source .venv/bin/activate; python3 -m poetry install --with=dev

.venv:
	python3 -m venv .venv

.PHONY: format
format: .venv   ## Apply format rules to the python code
	source .venv/bin/activate; black "${MODULE}"
	source .venv/bin/activate; black test

.PHONY: lint
lint:  ## Run linter on the python code
	source .venv/bin/activate; pylint "${MODULE}"

.PHONY: run
run:  ## Execute hello_world
	source .venv/bin/activate; python3 -m "${MODULE}"

.PHONY: test
test:  ## Run tests
	source .venv/bin/activate; python3 -m pytest

.PHONY: test-cov
test-cov:  ## Get coverage report
	source .venv/bin/activate; python3 -m \
	  pytest --cov=${MODULE}

.PHONY: doc
doc:  ## Generate documentation from the source code
	# TODO Update your module name
	source .venv/bin/activate; pdoc3 --force -o docs/ "${MODULE}"

