import datetime
from typing import Annotated

from fastapi import APIRouter, Query

from src.schemas.deposit import DateValidator, DepositCalculationResponse

deposit_router = APIRouter(prefix="/deposit", tags=["deposit"])

@deposit_router.get("/calculation", summary="Расчет депозита", response_model=DepositCalculationResponse)
async def deposit_calculation(
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
    ) -> dict[datetime.date, float]:
    """Получение результата расчета депозита

    Были мысли о реализации 2х методов: POST и GET. Сначала принять запрос на расчет, создать запись в бд,
    сам расчет провести, например, в Celery, сохранить результат. А отдельным методом получать результат
    по идентификатору. Такой подход мог бы раскрыться при возможности ввода большого числа месяцев, тк сложность
    расчета O(n). Плюс переиспользовать результаты для одинаковых входных параметров. Но от такого решения было решено
    отказаться тк в условиях задачи прописано ограничение на максимальное число месяцев - 60.
    """
    return {datetime.datetime.now().date(): 123.01}
