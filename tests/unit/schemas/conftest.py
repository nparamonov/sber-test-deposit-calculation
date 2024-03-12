import datetime

import pytest


@pytest.fixture()
def date() -> datetime.date:
    """Дата"""
    return datetime.date(2024, 1, 1)
