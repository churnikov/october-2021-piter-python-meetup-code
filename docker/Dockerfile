FROM python:3.9-slim

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-dev --no-interaction --no-ansi

COPY ./app  /code/app/

ENV LOGURU_AUTOINIT 0
