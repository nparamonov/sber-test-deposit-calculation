import datetime

import pytest

from src.dto.deposit import DepositPeriodMonthDTO
from src.models.deposit import DepositPeriodMonth


@pytest.mark.unit()
@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        pytest.param(
            DepositPeriodMonthDTO(date=datetime.date(2024, 1, 31), amount=10_000, periods=4, rate=6),
            {
                datetime.date(2024, 1, 31): 10050.00,
                datetime.date(2024, 2, 29): 10100.25,
                datetime.date(2024, 3, 31): 10150.75,
                datetime.date(2024, 4, 30): 10201.51,
            },
            id="end_of_month",
        ),
        pytest.param(
            DepositPeriodMonthDTO(date=datetime.date(2024, 11, 7), amount=100_000, periods=3, rate=10.5),
            {
                datetime.date(2024, 11, 7): 100875.00,
                datetime.date(2024, 12, 7): 101757.66,
                datetime.date(2025, 1, 7): 102648.04,
            },
            id="middle_of_month_next_year",
        ),
    ],
)
def test_deposit_period_month(data: DepositPeriodMonthDTO, expected_result: dict[datetime.date, float]) -> None:
    """Проверка модели расчета депозита"""
    accuracy = 0.01
    deposit = DepositPeriodMonth(data)
    result = deposit.calculate()
    assert len(result) == len(expected_result)
    for res, expected_res in zip(result.items(), expected_result.items(), strict=True):
        date, amount = res
        expected_date, expected_amount = expected_res
        assert date == expected_date
        assert abs(amount - expected_amount) < accuracy
