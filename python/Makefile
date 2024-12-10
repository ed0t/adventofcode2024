PYLINT_FLAGS = -E
# python_version  = 3.11.0
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
# current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))
current_dir := aoc2024

app_name            = advent_of_code_2024
version             = $(or $(VERSION), latest)
docker_registry     = co.relaytech
docker_image_name   = $(app_name):$(version)
docker_image_url    = $(docker_registry)/$(docker_image_name)

python_version  = 3.12.1
pip_version     = 23.0.1
poetry_version  = 1.6.1
additional_docker_build_args = --build-arg PYTHON_VERSION=$(python_version) --build-arg POETRY_VERSION=$(poetry_version) --build-arg OVERRIDE_PIP_VERSION=$(pip_version)


pyenv:
	@pyenv install -s $(python_version)
	@pyenv virtualenvs | grep "$(python_version)/envs/$(current_dir)" || pyenv virtualenv $(python_version) $(current_dir)
	@echo $(python_version)/envs/$(current_dir) > .python-version


pyenv-uninstall:
	@rm .python-version
	@pyenv uninstall -f $(current_dir)

.PHONY: build-image
build-image:
	docker build $(additional_docker_build_args) --pull  -t $(docker_image_url) .

.PHONY: install
install:
	poetry install

.PHONY: run
run: install
	poetry run python -m main

.PHONY: test
test: install
	poetry run pytest


.PHONY: pyenv pyenv-uninstall

