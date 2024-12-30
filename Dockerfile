FROM python:3.12.3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY django_project/* .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
