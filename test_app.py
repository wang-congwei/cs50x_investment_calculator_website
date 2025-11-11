import pytest
from app import month_calculate
from app import app


def test_month_calculate_basic():
    assert abs(month_calculate(100, 12) - 1280.93) < 1


def test_month_calculate_zero_rate():
    assert month_calculate(100, 0) == 1200


def test_month_calculate_zero_month():
    assert month_calculate(0, 12) == 0


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Investment" in response.data


def test_index_post_valid(client):
    response = client.post("/", data={
        "capital": "10000",
        "month_invest": "100",
        "invest_year": "5",
        "invest_rate": "10"
    })
    assert response.status_code == 200
    assert b"Total Assets" in response.data


def test_index_post_invalid_input(client):
    response = client.post("/", data={
        "capital": "-10000",
        "month_invest": "100",
        "invest_year": "5",
        "invest_rate": "10"
    })
    assert response.status_code == 400
    assert b"apology" in response.data.lower() or b"invalid" in response.data.lower()
