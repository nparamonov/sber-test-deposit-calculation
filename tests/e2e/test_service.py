import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


@pytest.mark.e2e()
def test_ping(client: TestClient) -> None:
    """Test /service/ping"""
    response = client.get("/service/ping")
    assert response.status_code == HTTP_200_OK
    assert response.text == "pong"
