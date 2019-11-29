build:
	pip install -r requirements.txt && \
	pip install -e .

tests:
	mypy args && \
	pytest --cov args

format:
	black -l 79 .
