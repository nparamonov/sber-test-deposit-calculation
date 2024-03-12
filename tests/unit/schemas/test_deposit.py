import datetime

import pytest

from src.config import DATE_FORMAT, FLOAT_PRECISION
from src.schemas.deposit import date_to_str, round_float, str_to_date


@pytest.mark.unit()
def test_date_to_str(date: datetime.date) -> None:
    """Проверка преобразования даты в строку"""
    assert date_to_str(date) == date.strftime(DATE_FORMAT)


@pytest.mark.unit()
def test_str_to_date_valid(date: datetime.date) -> None:
    """Проверка преобразования строки в дату"""
    assert str_to_date(date.strftime(DATE_FORMAT)) == date


@pytest.mark.unit()
def test_str_to_date_invalid() -> None:
    """Проверка преобразования строки в дату"""
    with pytest.raises(ValueError, match=f"time data 'abc' does not match format '{DATE_FORMAT}'"):
        str_to_date("abc")


@pytest.mark.unit()
def test_round_float() -> None:
    """Проверка округления float значений"""
    value = 1.1234
    assert round_float(value) == round(value, FLOAT_PRECISION)
