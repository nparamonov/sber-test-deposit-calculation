import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

QueryParamTypes = dict[str, str | int | float]

@pytest.mark.e2e()
def test_deposit_calculation(client: TestClient) -> None:
    """Test /deposit/calculation (success)"""
    params: QueryParamTypes = {
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10_000,
        "rate": 6,
    }
    response = client.get("/deposit/calculation", params=params)
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"31.01.2021": 10050.0, "28.02.2021": 10100.25, "31.03.2021": 10150.75}

@pytest.mark.e2e()
@pytest.mark.parametrize(
    "test_params",
    [
        # date
        {"date": "2021-01-31", "periods": 3, "amount": 10_000, "rate": 6},
        {"date": "abc", "periods": 3, "amount": 10_000, "rate": 6},
        {"date": "31.02.2021", "periods": 3, "amount": 10_000, "rate": 6},
        # periods
        {"date": "31.01.2021", "periods": -5, "amount": 10_000, "rate": 6},
        {"date": "31.01.2021", "periods": 0, "amount": 10_000, "rate": 6},
        {"date": "31.01.2021", "periods": 61, "amount": 10_000, "rate": 6},
        {"date": "31.01.2021", "periods": 3.5, "amount": 10_000, "rate": 6},
        # amount
        {"date": "31.01.2021", "periods": 3, "amount": 10_000.25, "rate": 6},
        {"date": "31.01.2021", "periods": 3, "amount": -5, "rate": 6},
        {"date": "31.01.2021", "periods": 3, "amount": 1_000, "rate": 6},
        {"date": "31.01.2021", "periods": 3, "amount": 10_000_000, "rate": 6},
        # rate
        {"date": "31.01.2021", "periods": 3, "amount": 10_000, "rate": -5},
        {"date": "31.01.2021", "periods": 3, "amount": 10_000, "rate": 0},
        {"date": "31.01.2021", "periods": 3, "amount": 10_000, "rate": 9},
    ],
)
def test_deposit_calculation_validation(client: TestClient, test_params: QueryParamTypes) -> None:
    """Test /deposit/calculation (валидация)"""
    response = client.get("/deposit/calculation", params=test_params)
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json().get("error") is not None
