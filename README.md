# October 2021 piter python meetup code

Example project that shows how to create, use and handle exceptions in python

# Идейная суть:

Тема доклада:

Цель доклада (основная мысль):

- Как работать с исключениями в python и обрабатывать их через наследование

Сформулировать темы и цели разделов докада
- В целом про программы и зачем в них исключения
  - Цель в том, чтобы познакомить слушателя с тем, что хорошие программы должны не только работать и быть полезными в
  опимистичных ситуациях, когда всё хорошо, а должны внятно себя вести и в случае каких либо ошибок (пример: zero division error)
- Рассказать про исключения в python
  - Цель: показать, что они тоже объекты и у них уже есть иерархия, в рамках которой можно работать.
- Ввести пример приложения
  - Цель: на примерах можно уже конкретно обозначать то, о чём хочется сказать
  - Идеи примеров: библиотека-калькулятор, библиотека-поисковик
- Показать парочку кастомных примеров созданных ошибок и показать проблему, что пользователь может захотеть обрабатывать наши ошибки
  - Цель: ввести базовый класс-исключение
- Дальше предложить с одной стороны общие ошибки, но всё же более частные
  (если калькулятор, то сделать BinaryOpException(left, right), если поисковик, то что что-то не нашлось и парметры, что искали)
- Показать, что дальше, с такими ошибками, можно делать rest api и иметь базовые аттрибуты с кодом ошибок и телом ошибки
- Можно делать cli приложения и оборачивать обработку в try except
- Цель: показать, что продуманная система ошибок может позволять делать гибкие приложения,
  дающие что-то осмысленное даже в исключительных ситуациях
- Конкретно показать, что можно в местах с потенциальным вызовом исключений делать сразу обработку ошибок и, потенциально, однообразную работу
  (например что-то не найдено и возвращать код 404)
- Суммировать:
  - Что в python можно работать с ошибками как с объектами и через наследование
  - Это удобно для того, чтобы разделять основную логику приложений и обработку ошибок
    (показать сравнение перемешанного возвращения информации об ошибке и разделённой обработки ошибок)

Составить план выступления

Сделать слайды с акцентами

Дата: 19 или 21 октября

# Полезные материалы:

## Для подготовки доклада

- https://habr.com/en/company/tinkoff/blog/576468/
- https://www.youtube.com/watch?v=T6Os27MKUCQ&t=2332s

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
