FROM python:3.10.0rc1-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt