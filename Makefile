.PHONY: test clean

test:
	tox

clean:
	rm -rf *.egg-info build dist .tox
