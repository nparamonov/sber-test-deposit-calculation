import datetime

from pydantic import ConfigDict, RootModel
from pydantic.functional_validators import BeforeValidator

from src.config import DATE_FORMAT, FLOAT_PRECISION


def str_to_date(value: str) -> datetime.date:
    """Преобразовать строку dd.mm.YYYY в дату"""
    return datetime.datetime.strptime(value, DATE_FORMAT).date()


def date_to_str(value: datetime.date) -> str:
    """Преобразовать дату в строку dd.mm.YYYY"""
    return value.strftime(DATE_FORMAT)


def round_float(value: float) -> float:
    """Округлить число до 2 знаков после запятой"""
    return round(value, FLOAT_PRECISION)


DateValidator = BeforeValidator(str_to_date)

class DepositCalculationResponse(RootModel[dict[datetime.date, float]]):
    """Модель ответа с результатами расчета депозита"""
    model_config = ConfigDict(
        json_encoders={
            datetime.date: date_to_str,
            float: round_float,
        },
        json_schema_extra={
            "examples": [
                {"31.01.2021": 10050, "28.02.2021": 10100.25, "31.03.2021": 10150.75},
            ],
        },
    )
