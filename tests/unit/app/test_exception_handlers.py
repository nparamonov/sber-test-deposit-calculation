import pytest
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request

from src.app.exception_handlers import request_validation_exception_handler


@pytest.mark.unit()
@pytest.mark.parametrize(
    ("errors", "response"),
    [
        pytest.param(
            [{"msg": "msg", "loc": "loc", "input": "input"}],
            b'{"error":"msg: loc = input"}',
            id="single",
        ),
        pytest.param(
            [{"msg": "msg1", "loc": "loc1", "input": "input1"}, {"msg": "msg2", "loc": "loc2", "input": "input2"}],
            b'{"error":"msg1: loc1 = input1. msg2: loc2 = input2"}',
            id="multiple",
        ),
    ],
)
@pytest.mark.asyncio()
async def test_request_validation_exception_handler(errors: list[dict[str, str]], response: bytes) -> None:
    """Тест обработчика ошибок валидации при единичной ошшибке и нескольких ошибках"""
    request = Request(scope={"type": "http"})
    exc = RequestValidationError(errors=errors)

    res = await request_validation_exception_handler(request, exc)

    assert res.body == response
