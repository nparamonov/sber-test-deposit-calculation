from collections.abc import Callable, Coroutine
from typing import Any

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_400_BAD_REQUEST


async def request_validation_exception_handler(_request: Request, exc: RequestValidationError) -> JSONResponse:
    """Обработчик ошибки RequestValidationError

    По условиям задачи должен быть ключ "error" с текстом ошибки, поэтому вытаскиваем сообщение от pydantic.
    При необходимости, подробную структуру можно получить: fastapi.encoders.jsonable_encoder(exc.errors())
    """
    msg = ". ".join([f"{error['msg']}: {error['loc']} = {error['input']}" for error in exc.errors()])

    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"error": msg},
    )

exception_handlers: dict[int | type[Exception], Callable[[Request, Any], Coroutine[Any, Any, Response]]] = {
    RequestValidationError: request_validation_exception_handler,
}

openapi_responses: dict[int | str, dict[str, Any]] = {
    "400": {
        "description": "Ошибка валидации",
        "content": {
            "application/json": {
                "schema": {
                    "title": "Ошибка валидации",
                    "type": "object",
                    "properties": {
                        "error": {
                            "title": "Описание ошибки",
                            "type": "string",
                        },
                    },
                },
            },
        },
    },
}
