build:
	pip install poetry && \
	poetry install

test:
	pytype args && \
	pytest -s --cov args

pep8_checks:
	flake8

format:
	black -l 79 .
