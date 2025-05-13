# tests/test_models.py

import pytest
from app import create_app, db
from app.models import DoctorAvailability, Appointment
from datetime import datetime

@pytest.fixture
def app():
    # Create an instance of the Flask app with a testing config
    app = create_app('testing')  # Assuming 'testing' config is set up in your app
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db():
    # Initialize the database with the test data
    db.create_all()

    # Create some test data
    availability = DoctorAvailability(
        doctor_id=1,
        available_from="2025-04-16 09:00:00",
        available_to="2025-04-16 17:00:00",
    )
    db.session.add(availability)
    db.session.commit()

    yield db  # This will allow you to access db for tests

    # Teardown after each test
    db.drop_all()

def test_doctor_availability(init_db):
    availability = DoctorAvailability.query.first()
    assert availability is not None
    assert availability.doctor_id == 1
    assert availability.available_from == "2025-04-16 09:00:00"
    assert availability.available_to == "2025-04-16 17:00:00"

def test_appointment_creation(init_db):
    availability = DoctorAvailability.query.first()
    appointment = Appointment(
        doctor_availability_id=availability.id,
        patient_name="John Doe",
        appointment_time=datetime(2025, 4, 16, 10, 0)
    )
    db.session.add(appointment)
    db.session.commit()

    saved_appointment = Appointment.query.first()
    assert saved_appointment is not None
    assert saved_appointment.patient_name == "John Doe"
    assert saved_appointment.appointment_time == datetime(2025, 4, 16, 10, 0)
