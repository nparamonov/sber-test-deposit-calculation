import datetime
from typing import Annotated

from fastapi import Query

from src.dto.deposit import DepositPeriodMonthDTO
from src.models.deposit import DepositPeriodMonth
from src.schemas.deposit import DateValidator
from src.services.deposit import DepositCalculationService


def get_deposit_calculation_service(
    date: Annotated[
        datetime.date,
        Query(description="Дата заявки", examples=["31.01.2021"]),
        DateValidator,
    ],
    periods: Annotated[
        int,
        Query(ge=1, le=60, description="Количество месяцев по вкладу", examples=[3]),
    ],
    amount: Annotated[
        int,
        Query(ge=10_000, le=3_000_000, description="Сумма вклада", examples=[10_000]),
    ],
    rate: Annotated[
        float,
        Query(ge=1, le=8, description="Процент по вкладу", examples=[6]),
    ],
) -> DepositCalculationService:
    """Инициализация логики расчета депозита"""
    data = DepositPeriodMonthDTO(date=date, amount=amount, periods=periods, rate=rate)
    deposit = DepositPeriodMonth(data)
    return DepositCalculationService(deposit)
