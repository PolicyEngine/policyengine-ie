all: install format test

documentation:
	myst build docs -o docs/_build

format:
	black . -l 79
	linecheck . --fix

install:
	uv pip install --system -e .[dev]

test:
	uv run pytest policyengine_ie/tests -v

test-cov:
	uv run pytest policyengine_ie/tests --cov=policyengine_ie --cov-report=term-missing

test-lite:
	uv run pytest policyengine_ie/tests/policy -v

build:
	python -m build

changelog:
	build-changelog changelog.yaml --output CHANGELOG.md --start-from 0.1.0

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build dist *.egg-info .coverage htmlcov

.PHONY: all documentation format install test test-cov test-lite build changelog clean