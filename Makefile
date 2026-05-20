.PHONY: install test clean

install:
	poetry install

test:
	poetry run flake8 wave_reader/ tests/
	poetry run mypy wave_reader --ignore-missing-imports
	poetry run pytest ./tests

clean:
	rm -rf *.egg-info build dist .venv .coverage .pytest_cache coverage.xml .mypy_cache site

mkdocs:
	mkdocs build --clean

pytest:
	poetry run pytest --cov wave_reader tests
