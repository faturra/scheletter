FROM python:3.9.7-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/

# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "makemigrations"]
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "initgroups"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
