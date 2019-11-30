build:
	pip install -r requirements.txt && \
	pip install -e .

tests:
	mypy args --ignore-missing-imports && \
	pytest -s --cov args

format:
	black -l 79 .
