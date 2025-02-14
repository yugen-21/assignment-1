import pytest
from app import app

@pytest.fixture
def client():
    # Set up a test client for our Flask app
    with app.test_client() as client:
        yield client

def test_home(client):
    # Test the home page is rendered correctly
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Flask App!" in response.data
    assert b"This is a simple web page served using Flask." in response.data
