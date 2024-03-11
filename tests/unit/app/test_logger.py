import logging

import pytest

from src.app.logger import init_logging


@pytest.mark.unit()
def test_init_logging_default() -> None:
    """Тест инициализации логирования с параметрами по умолчанию"""
    init_logging()

@pytest.mark.skip(reason="Pytest переопределяет настройки logging")
@pytest.mark.unit()
def test_init_logging_level() -> None:
    """Тест инициализации логирования с кастомным уровнем"""
    init_logging(log_level=logging.DEBUG)
    assert logging.root.level == logging.DEBUG

@pytest.mark.skip(reason="Pytest переопределяет настройки logging")
@pytest.mark.unit()
def test_init_logging_handler() -> None:
    """Тест инициализации логирования с кастомным хендлером"""
    custom_handler = logging.StreamHandler()
    init_logging(handler=custom_handler)
    assert logging.root.handlers == [custom_handler]

@pytest.mark.skip(reason="Pytest переопределяет настройки logging")
@pytest.mark.unit()
def test_init_logging_custom_loggers() -> None:
    """Тест инициализации логирования с кастомными логгерами"""
    custom_loggers = ["custom_logger1", "custom_logger2"]
    init_logging(custom_loggers=custom_loggers)
    for logger_name in custom_loggers:
        logger = logging.getLogger(logger_name)
        assert logger.handlers == [logging.root.handlers[0]]
        assert logger.propagate is False
        assert logger.level == logging.root.level
