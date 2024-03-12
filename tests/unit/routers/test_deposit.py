import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


@pytest.mark.unit()
def test_deposit_calculation(client_override: TestClient, calculation_output_api: dict[str, float]) -> None:
    """Test /deposit/calculation (success)"""
    response = client_override.get("/deposit/calculation")
    assert response.status_code == HTTP_200_OK
    assert response.json() == calculation_output_api
