FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements/requirements.txt

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]