build:
	pip install -r requirements.txt && \
	pip install -e .

tests:
	pytype args && \
	pytest -s --cov args

format:
	black -l 79 .
