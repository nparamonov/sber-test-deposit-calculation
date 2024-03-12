import datetime

import pytest

from src.services.deposit import DepositCalculationService


@pytest.mark.unit()
def test_deposit_calculation_service(deposit_service: DepositCalculationService,
                                     deposit_output_params: dict[datetime.date, float]) -> None:
    """Тест сервиса расчета депозита"""
    assert deposit_service.calculate() == deposit_output_params
