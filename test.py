from unittest.mock import ANY
import http.client

# First party modules
from app import app
import pytest



@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """

    #app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_checkout3(client):
    response = client.get('/checkout?ids=1,1,1')
    result = response.json
    assert response.status_code == 200
    assert result["total_price"] == 200


def test_checkout5(client):
    response = client.get('/checkout?ids=1,1,1,1,2')
    result = response.json
    assert response.status_code == 200
    assert result["total_price"] == 380


def test_singleitem(client):
    response = client.get('/checkout?ids=1')
    result = response.json
    assert response.status_code == 200
    assert result["total_price"] == 100


def test_withoutparameter(client):
    response = client.get('/checkout?ids=')
    assert response.status_code == 500


