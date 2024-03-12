import datetime

import pytest
from fastapi.testclient import TestClient

from src.dependencies.deposit import get_deposit_calculation_service
from src.dto.deposit import DepositPeriodMonthDTO
from src.main import deposit_calculation_app
from src.models.deposit import DepositPeriodMonth
from src.services.deposit import DepositCalculationService


@pytest.fixture()
def client(request: pytest.FixtureRequest) -> TestClient:
    """Возвращает экземпляр приложения FastAPI для тестирования"""
    dependency_overrides  = getattr(request, "param", {})
    deposit_calculation_app.app.dependency_overrides = dependency_overrides
    return TestClient(deposit_calculation_app.app)


CALCULATION_OUTPUT_SERVICE = {datetime.date(2024, 1, 1): 1000.5, datetime.date(2024, 2, 1): 2000.5}
CALCULATION_OUTPUT_API = {"01.01.2024": 1000.5, "01.02.2024": 2000.5}


class DepositCalculationServiceOverride(DepositCalculationService):
    """Переопределяем класс для получения тестовых результатов"""
    output: dict[datetime.date, float]

    def calculate(self) -> dict[datetime.date, float]:
        """Рассчитать депозит

        Returns:
            dict[datetime.date, float]: состояние депозита.
                Ключ - конечная дата периода, значение - сумма депозита за этот период.
        """
        return self.output


def get_deposit_calculation_service_override() -> DepositCalculationServiceOverride:
    """Инициализация логики расчета депозита"""
    data = DepositPeriodMonthDTO(date=datetime.date(2024, 1, 1), amount=10, periods=3, rate=6)
    deposit = DepositPeriodMonth(data)
    service = DepositCalculationServiceOverride(deposit)
    service.output = CALCULATION_OUTPUT_SERVICE
    return service


@pytest.fixture()
def client_override() -> TestClient:
    """Возвращает экземпляр приложения FastAPI для тестирования"""
    dependency_overrides = {get_deposit_calculation_service: get_deposit_calculation_service_override}
    deposit_calculation_app.app.dependency_overrides = dependency_overrides
    return TestClient(deposit_calculation_app.app)

@pytest.fixture()
def calculation_output_api() -> dict[str, float]:
    """Ответ АПИ с результатом расчета"""
    return CALCULATION_OUTPUT_API
