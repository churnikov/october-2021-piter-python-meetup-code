# October 2021 piter python meetup code

Example project that shows how to create, use and handle exceptions in python

# Полезные материалы:

## Ссылки на полезные материалы

- [Шаблон репозитория](https://github.com/churnikov/cookiecutter-python)
- [Репо с демо-приложением](https://github.com/churnikov/october-2021-piter-python-meetup-code)
- [Обработка ошибок в flask](https://flask.palletsprojects.com/en/2.0.x/errorhandling/)
- [Обработка ошибок в fastapi](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- Как REST API могут отвечать ошибками
    - https://blog.restcase.com/rest-api-error-handling-problem-details-response/
    - [Спецификация ошибок REST API](https://datatracker.ietf.org/doc/html/rfc7807)

# Development

## Installing dependencies

This project uses [poetry 1.1.3](http://python-poetry.org) for its dependency management. If you don't have poetry installed please, install it via the following command:

```console
$ POETRY_VERSION=1.1.3 curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

To install dependencies please use the following command:

```console
poetry install
```

## Code formatting

To format code you can use [pre-commit](http://pre-commit.com).

Firstly, you need to install pre-commit hooks:

```console
$ pre-commit install
```

Then you can run code format:

```console
$ pre-commit run --all-files
```

These hooks will also be executed before every commit.


## Project structure:

```
├── CHANGELOG.md                    <- File that describes notable changes of this project
├── README.md                       <- file you are reading
├── app                             <- Main soure code of application
│   ├── __init__.py                 <- Says that folder is module
│   ├── api                         <- Flask app example
│   │   ├── __init__.py             <- Says that folder is module
│   │   ├── api.py                  <- Implementation of REST API routes
│   │   ├── error_handlers.py       <- Implemetation of Flask error handlers
│   │   └── main.py                 <- Main file with configuration
│   ├── cli                         <- Comand line tool implementation
│   │   ├── __init__.py             <- Says that folder is module
│   │   ├── api.py                  <- Comandline tools implementation
│   │   └── main.py                 <- Main file with configuration
│   ├── crud.py                     <- Create read update and delete operations
│   ├── errors.py                   <- Custom errors implementation
│   ├── log.py                      <- Loguru sink and formatter
│   ├── main.py                     <- Main file with configuration
│   ├── py.typed                    <- This file marks module as typed
│   ├── settings.py                 <- File that loads configurations into settings object
│   └── validators.py               <- Input data validators
├── churikov-presentation.key       <- Presentation for meetup
├── docker                          <- Files related to deployment via docker
│   └── Dockerfile
├── .flake8                         <- Settings for flake8
├── mypy.ini                        <- Settings for mypy
├── .env.sample                     <- Excample of .env file. You can use it to set environment variables.
│                                      (You can setup usage of env variables by copying it into file with name .env)
├── .gitignore                      <- List of files for git to ignore
├── poetry.lock                     <- Complete and locked dependency graph of this project
├── pyproject.toml                  <- Dependencies and settings of black and isort tool. execute in console `poetry install` to install them. `poetry add LIB_NAME` to add new dependency.
└── tests                           <- Folder for tests of this application
    └── test_api.py
```

## How to run api

```console
$ export FLASK_APP=app.api:app
$ flask run
```

## How to run cli

```console
$ churstore add-data data
```

# About original template

Repository created from [churnikov:cookiecutter-python](https://github.com/churnikov/cookiecutter-python) using template version [2be81a751896bce7874f63b546111d1faea02d59](https://github.com/churnikov/cookiecutter-python/commit/2be81a751896bce7874f63b546111d1faea02d59).
