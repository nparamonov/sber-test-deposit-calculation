import datetime
from dataclasses import dataclass

import pytest

from src.dto.deposit import DepositDTO
from src.models.deposit import Deposit
from src.services.deposit import DepositCalculationService


@pytest.fixture()
def deposit_output_params() -> dict[datetime.date, float]:
    """Результат расчета депозита"""
    return {datetime.date(2021, 1, 1): 1000, datetime.date(2021, 2, 1): 2000}


@dataclass
class DepositDTOMock(DepositDTO):
    """Мок DTO исходные данные для расчета депозита"""
    output: dict[datetime.date, float]


@pytest.fixture()
def deposit_data(deposit_output_params: dict[datetime.date, float]) -> DepositDTOMock:
    """Изсходные данные для расчета депозита"""
    return DepositDTOMock(date=datetime.date(2024, 1, 1), amount=100, output=deposit_output_params)


class DepositMock(Deposit[DepositDTOMock]):
    """Мок реализация расчета депозита"""

    def calculate(self) -> dict[datetime.date, float]:
        """Рассчитать депозит

        Returns:
            dict[datetime.date, float]: состояние депозита.
                Ключ - конечная дата периода, значение - сумма депозита за этот период.
        """
        return self._data.output


@pytest.fixture()
def deposit_model(deposit_data: DepositDTOMock) -> DepositMock:
    """Мок модели депозита"""
    return DepositMock(deposit_data)


@pytest.fixture()
def deposit_service(deposit_model: Deposit[DepositDTOMock]) -> DepositCalculationService:
    """Сервис расчета депозита"""
    return DepositCalculationService(deposit_model)
