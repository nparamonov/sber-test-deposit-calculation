import datetime
from dataclasses import dataclass


@dataclass
class DepositDTO:
    """DTO исходные данные для расчета депозита"""
    date: datetime.date
    amount: int


@dataclass
class DepositPeriodMonthDTO(DepositDTO):
    """DTO исходные данные для расчета депозита по месяцам"""
    periods: int
    rate: float
