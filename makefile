build:
	pip install -r requirements.txt && \
	pip install -e .

tests:
	pytest --cov args

format:
	black -l 79 .
