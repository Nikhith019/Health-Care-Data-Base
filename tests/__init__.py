# tests/__init__.py

import pytest
from app import create_app, db
from flask import Flask
from app.models import DoctorAvailability

@pytest.fixture
def app():
    # Create a Flask app instance for testing
    app = create_app('testing')  # Ensure 'TestingConfig' exists in config.py

    with app.app_context():
        yield app  # Provide the app with an active app context

@pytest.fixture
def client(app):
    return app.test_client()

def init_db(app):
    with app.app_context():
        db.create_all()

        # Add sample data
        availability = DoctorAvailability(
            doctor_id=1,
            available_from="2025-04-16 09:00:00",
            available_to="2025-04-16 17:00:00",
        )
        db.session.add(availability)
        db.session.commit()

        yield db
        db.drop_all()
        
def test_create_app(app):
    # Confirm app creation and config
    assert isinstance(app, Flask)
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///test.db'
    assert app.config['TESTING'] is True

def test_database_initialization(init_db):
    # Verify sample data is inserted
    availability = DoctorAvailability.query.first()
    assert availability is not None
    assert availability.doctor_id == 1
    assert availability.available_from == "2025-04-16 09:00:00"

def test_routes_initialization(client):
    # Simple route test (assuming `/` route is defined)
    response = client.get('/')
    assert response.status_code == 200