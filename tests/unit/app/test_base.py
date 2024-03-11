import pytest
from fastapi import APIRouter, FastAPI

from src.app.base import DepositCalculationApp


@pytest.mark.unit()
def test_deposit_calculation_app() -> None:
    """Тест приложения DepositCalculationApp"""
    router = APIRouter()
    router.add_api_route(methods=["GET"], path="/test", endpoint=lambda: "test_response")
    app = DepositCalculationApp(
        app_type=FastAPI,
        main_router=router,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        swagger_ui_oauth2_redirect_url=None,
    )
    assert isinstance(app.app, FastAPI)
    test_routes = [route for route in app.app.routes if route.path == "/test"]  # type: ignore[attr-defined]
    assert len(test_routes) == 1, "Не обнаружено роута /test"
