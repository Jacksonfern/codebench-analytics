PROJECT_PATH=codebench_analytics/

.PHONY: setup
setup:
	@poetry env use 3.11
	@poetry install

.PHONY: lint
lint:
	@poetry run black $(PROJECT_PATH) $(BLACK_OPTIONS)
	@poetry run ruff check $(PROJECT_PATH) $(RUFF_OPTIONS)

.PHONY: format
format: RUFF_OPTIONS := --fix
format: format lint
