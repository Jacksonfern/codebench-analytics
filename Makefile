PROJECT_PATH=codebench_analytics/

BLACK_OPTIONS := --check

.PHONY: setup
setup:
	@poetry env use 3.11
	@poetry install

.PHONY: lint
lint:
	@poetry run black $(BLACK_OPTIONS) $(PROJECT_PATH)
	@poetry run ruff check $(PROJECT_PATH) $(RUFF_OPTIONS)

.PHONY: format
format: RUFF_OPTIONS := --fix
format: BLACK_OPTIONS :=
format: lint
