import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_login(client):
    # Try login with valid credentials
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'test'
    }, follow_redirects=True)
    print(response.data.decode())  # Print response for debugging
    assert b'Welcome Test User!' in response.data or b'dashboard' in response.data

def test_login_invalid(client):
    # Try login with invalid credentials
    response = client.post('/login', data={
        'email': 'wrong@email.com',
        'password': 'wrongpass'
    }, follow_redirects=True)
    print(response.data.decode())  # Print response for debugging
    assert b'Invalid credentials' in response.data