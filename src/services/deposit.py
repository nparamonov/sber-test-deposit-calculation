import datetime

from src.dto.deposit import DepositDTO
from src.models.deposit import Deposit


class DepositCalculationService:
    """Сервис расчета депозита"""
    def __init__(self, deposit: Deposit[DepositDTO]) -> None:
        """Конструктор

        Args:
            deposit (Deposit[DepositDTO]): Модель расчета депозита
        """
        self._deposit = deposit

    def calculate(self) -> dict[datetime.date, float]:
        """Рассчитать депозит

        Returns:
            dict[datetime.date, float]: состояние депозита.
                Ключ - конечная дата периода, значение - сумма депозита за этот период.
        """
        return self._deposit.calculate()
