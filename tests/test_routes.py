# tests/test_routes.py

import pytest
from app import create_app, db
from app.models import DoctorAvailability, Appointment
from datetime import datetime

@pytest.fixture
def app():
    app = create_app('testing')  # Assuming 'testing' config is set up in your app
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db():
    db.create_all()

    availability = DoctorAvailability(
        doctor_id=1,
        available_from="2025-04-16 09:00:00",
        available_to="2025-04-16 17:00:00",
    )
    db.session.add(availability)
    db.session.commit()

    yield db

    db.drop_all()

def test_create_appointment(client, init_db):
    availability = DoctorAvailability.query.first()
    response = client.post('/appointments', json={
        'doctor_availability_id': availability.id,
        'patient_name': 'Jane Smith',
        'appointment_time': '2025-04-16 10:30:00'
    })

    assert response.status_code == 201
    assert response.json['patient_name'] == 'Jane Smith'

def test_get_appointments(client, init_db):
    response = client.get('/appointments')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_appointment_by_id(client, init_db):
    appointment = Appointment.query.first()
    response = client.get(f'/appointments/{appointment.id}')
    assert response.status_code == 200
    assert response.json['patient_name'] == appointment.patient_name
