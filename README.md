# sber-test-deposit-calculation
Тестовое задание. Сбер. Сервис для расчета депозита

## Задача

![Задача](/docs/task/task.png)

Алгоритм расчета: [/docs/task/example.xlsx](/docs/task/example.xlsx)

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
