import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from sample_app import sample

def test_ejemploBasico():
    assert 1 + 1 == 2

@pytest.fixture
def client():
    sample.config['TESTING'] = True
    with sample.test_client() as client:
        yield client

def test_home_route_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200 #nosec B101