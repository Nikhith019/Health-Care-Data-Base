import pytest
from app import create_app, db
from app.models import User
from flask import jsonify

@pytest.fixture
def app():
    app = create_app('testing')  # Ensure 'testing' config is used in app
    with app.app_context():
        yield app  # Provide the app with an active app context

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db(app):
    """Initialize and create the database."""
    with app.app_context():
        db.create_all()

        # Create a test user for authentication
        user = User(username="testuser", password="testpassword")
        db.session.add(user)
        db.session.commit()

        yield db
        db.drop_all()

def test_register(client, init_db):
    """Test the registration endpoint."""
    response = client.post('/auth/register', json={
        'username': 'newuser',
        'password': 'newpassword'
    })

    assert response.status_code == 201
    assert 'access_token' in response.json  # JWT token should be returned

def test_login(client, init_db):
    """Test the login endpoint."""
    response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })

    assert response.status_code == 200
    assert 'access_token' in response.json  # JWT token should be returned

def test_login_invalid_credentials(client, init_db):
    """Test login with invalid credentials."""
    response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'wrongpassword'
    })

    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'

def test_protected_route(client, init_db):
    """Test a protected route with valid and invalid JWT tokens."""
    # Log in to get a token
    login_response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    token = login_response.json['access_token']

    # Access protected route with valid token
    response = client.get('/protected', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Protected content'

    # Access protected route with invalid token
    response = client.get('/protected', headers={
        'Authorization': 'Bearer invalid_token'
    })
    assert response.status_code == 401
    assert response.json['message'] == 'Token is invalid or expired'

