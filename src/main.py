from fastapi import FastAPI

from .app.base import DepositCalculationApp
from .app.exception_handlers import exception_handlers, openapi_responses
from .app.logger import colored_handler, init_logging
from .config import CUSTOM_LOGGERS, LOG_LEVEL
from .routers import main_router

init_logging(LOG_LEVEL, colored_handler, CUSTOM_LOGGERS)

deposit_calculation_app = DepositCalculationApp(
    app_type=FastAPI,
    main_router=main_router,
    exception_handlers=exception_handlers,
    responses=openapi_responses,
)
