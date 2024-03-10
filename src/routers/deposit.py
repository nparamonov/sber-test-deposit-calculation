import datetime
from typing import Annotated

from fastapi import APIRouter, Depends

from src.dependencies.deposit import get_deposit_calculation_service
from src.schemas.deposit import DepositCalculationResponse
from src.services.deposit import DepositCalculationService

deposit_router = APIRouter(prefix="/deposit", tags=["deposit"])

@deposit_router.get("/calculation", summary="Расчет депозита", response_model=DepositCalculationResponse)
async def deposit_calculation(
    service: Annotated[DepositCalculationService, Depends(get_deposit_calculation_service)],
) -> dict[datetime.date, float]:
    """Получение результата расчета депозита

    Были мысли о реализации 2х методов: POST и GET. Сначала принять запрос на расчет, создать запись в бд,
    сам расчет провести, например, в Celery, сохранить результат. А отдельным методом получать результат
    по идентификатору. Такой подход мог бы раскрыться при возможности ввода большого числа месяцев, тк сложность
    расчета O(n). Плюс переиспользовать результаты для одинаковых входных параметров. Но от такого решения было решено
    отказаться тк в условиях задачи прописано ограничение на максимальное число месяцев - 60.
    """
    return service.calculate()
