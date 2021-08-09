.PHONY: test clean

test:
	tox

clean:
	rm -rf *.egg-info build dist .tox .coverage .pytest_cache coverage.xml .mypy_cache site

mkdocs:
	mkdocs build --clean

pytest:
	pytest --cov-config=.coveragerc --cov wave_reader tests
