import calendar
import datetime
from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import Generic, TypeVar

from src.dto.deposit import DepositDTO, DepositPeriodMonthDTO

T_co = TypeVar("T_co", bound=DepositDTO, covariant=True)


class Deposit(ABC, Generic[T_co]):
    """Абстрактная модель депозита"""
    def __init__(self, data: T_co) -> None:
        """Конструктор класса

        Args:
            data (T): Исходные данные для расчета депозита
        """
        self._data = data

    @abstractmethod
    def calculate(self) -> dict[datetime.date, float]:
        """Рассчитать депозит

        Returns:
            dict[datetime.date, float]: состояние депозита.
                Ключ - конечная дата периода, значение - сумма депозита за этот период.
        """


class DepositPeriodMonth(Deposit[DepositPeriodMonthDTO]):
    """Одна из реализаций расчета депозита, по месяцам"""
    def __init__(self, data: DepositPeriodMonthDTO) -> None:
        """Конструктор класса

        Args:
            data (T): Исходные данные для расчета депозита
        """
        super().__init__(data)
        self._multiplier = 1 + self._data.rate / 12 / 100

    def calculate(self) -> dict[datetime.date, float]:
        """Рассчитать депозит

        Returns:
            dict[datetime.date, float]: состояние депозита.
                Ключ - конечная дата периода, значение - сумма депозита за этот период.
        """
        calculator = self._calculate_deposit(self._data.date, self._data.amount, self._data.periods)
        return dict(calculator)

    def _calculate_deposit(self,
                           date: datetime.date,
                           amount: float,
                           periods: int,
                           ) -> Generator[tuple[datetime.date, float], None, None]:
        """Расчет по количеству месяцев

        Args:
            date (datetime.date): Дата заявки
            amount (float): Сумма вклада
            periods (int): Количество месяцев по вкладу

        Yields:
            Generator[tuple[datetime.date, float], None, None]: состояние депозита.
                Ключ - конечная дата периода, значение - сумма депозита за этот период.
        """
        for _ in range(periods):
            amount *= self._multiplier
            yield date, amount
            date = self._next_month_date(date)

    def _next_month_date(self, current_date: datetime.date) -> datetime.date:
        """Добавить месяц к дате

        Args:
            current_date (datetime.date): Начальная дата

        Returns:
            datetime.date: Соответствующая дата в следующем месяце

        Добавляет месяц к переданной дате, например, 04.06.2021 -> 04.07.2021.
        Обрабатывает дни в конце месяца, например, 31.01.2021 -> 28.02.2021, 28.02.2021 -> 31.03.2021.
        """
        current_or_next_year = current_date.year + current_date.month // 12
        next_month_mod_12 = current_date.month % 12 + 1
        days_in_next_month = calendar.monthrange(current_or_next_year, next_month_mod_12)[1]
        days_in_current_month = calendar.monthrange(current_date.year, current_date.month)[1]
        if current_date.day == days_in_current_month or current_date.day > days_in_next_month:
            next_month_day = days_in_next_month
        else:
            next_month_day = current_date.day
        return datetime.date(current_or_next_year, next_month_mod_12, next_month_day)
