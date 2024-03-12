# sber-test-deposit-calculation
Тестовое задание. Сбер. Сервис для расчета депозита

[![pytest](https://img.shields.io/github/actions/workflow/status/nparamonov/sber-test-deposit-calculation/pytest.yml?branch=main&label=pytest&logo=pytest)](https://github.com/nparamonov/sber-test-deposit-calculation/actions/workflows/pytest.yml)
[![codecov](https://img.shields.io/codecov/c/github/nparamonov/sber-test-deposit-calculation/main?label=coverage&logo=codecov&token=YZZ21OI7AG)](https://codecov.io/gh/nparamonov/sber-test-deposit-calculation)
[![mypy](https://img.shields.io/github/actions/workflow/status/nparamonov/sber-test-deposit-calculation/mypy.yml?branch=main&label=mypy&logo=python)](https://github.com/nparamonov/sber-test-deposit-calculation/actions/workflows/mypy.yml)
[![ruff](https://img.shields.io/github/actions/workflow/status/nparamonov/sber-test-deposit-calculation/ruff.yml?branch=main&label=ruff&logo=ruff)](https://github.com/nparamonov/sber-test-deposit-calculation/actions/workflows/ruff.yml)
[![deptry](https://img.shields.io/github/actions/workflow/status/nparamonov/sber-test-deposit-calculation/deptry.yml?branch=main&label=deptry&logo=deptry)](https://github.com/nparamonov/sber-test-deposit-calculation/actions/workflows/deptry.yml)

## Задача

![Задача](/docs/task/task.png)

Алгоритм расчета: [/docs/task/example.xlsx](/docs/task/example.xlsx)

## Запуск

Собрать образ

```shell
docker build -t deposit-calculation --target=runtime .
```
Запустить контейнер

```shell
docker run --name deposit-calculation-api -p 8000:8000 -e LOG_LEVEL=INFO deposit-calculation
```

## Разработка

### Установка

Клонировать репозиторий и перейти в каталог проекта:

```shell
git clone https://github.com/nparamonov/sber-test-deposit-calculation.git
cd sber-test-deposit-calculation
```

Установить Poetry (https://python-poetry.org/docs/#installation), например:

```shell
pip install poetry
```

Установить зависимости:

```shell
poetry install
```

Активировать виртуальное окружение:

```shell
poetry shell
```

### Запуск

Для запуска приложения необходимо предварительно активировать окружение `poetry shell`,
либо запускать через команду `poetry run`.

Пример запуска для Linux:

```shell
uvicorn src.main:deposit_calculation_app.app --loop uvloop --no-server-header --host 127.0.0.1 --port 8008
```
Для Windows uvloop недоступен, поэтому необходимо либо указать `--loop auto`, либо исключить данный параметр.

Полный список доступных параметров: https://www.uvicorn.org/deployment/#running-from-the-command-line

### Тесты

Запуск тестов

```shell
pytest -v tests
```

Есть возможность запускать отдельно End-to-end и Unit тесты:

```shell
pytest -m e2e
pytest -m unit
```

Coverage:

```shell
coverage run -m pytest -m unit && coverage report
```

### Линтеры, тайп чекеры

```shell
mypy .
ruff check .
deptry .
```
