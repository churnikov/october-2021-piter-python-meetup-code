FROM python:3.9-slim

RUN poetry config virtualenvs.create false

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-dev --no-interaction --no-ansi

COPY ./app  /code/app/

ENV LOGURU_AUTOINIT 0
ENV FLASK_APP code.app.api:app
ENV ENV production

ENTRYPOINT flask run --ip 0.0.0.0
