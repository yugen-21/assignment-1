import sys
import os
import pytest

# Dynamically add the project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Now pytest will correctly find app.py

@pytest.fixture
def client():
    """Set up a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test if the homepage loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Flask App!" in response.data
    assert b"This is a simple web page served using Flask." in response.data
