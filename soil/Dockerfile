FROM python:3.11-slim-buster

RUN mkdir /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install psycopg2-binary
RUN pip3 install -r requirements.txt