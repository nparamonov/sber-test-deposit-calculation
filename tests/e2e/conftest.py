import pytest
from fastapi.testclient import TestClient

from src.main import deposit_calculation_app


@pytest.fixture()
def client() -> TestClient:
    """Возвращает экземпляр приложения FastAPI для тестирования"""
    return TestClient(deposit_calculation_app.app)
