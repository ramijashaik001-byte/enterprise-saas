.PHONY: install run test docker-build docker-run

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

docker-build:
	docker build -t enterprise-saas-hrms .

docker-run:
	docker run -p 8000:8000 enterprise-saas-hrms
