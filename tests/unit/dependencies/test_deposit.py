import datetime

import pytest

from src.dependencies.deposit import get_deposit_calculation_service
from src.services.deposit import DepositCalculationService


@pytest.mark.unit()
def test_get_deposit_calculation_service() -> None:
    """Тест депенденси для инициализации сервиса"""
    res = get_deposit_calculation_service(date=datetime.date.today(), periods=5, amount=10_000, rate=6)
    assert isinstance(res, DepositCalculationService)
