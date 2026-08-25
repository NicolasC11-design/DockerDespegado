import pytest
from backend.sample_app import app  # Importa la instancia de tu aplicación Flask

def test_ejemploBasico():
    assert 1 + 1 == 2

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200