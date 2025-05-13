# test_utils.py
import pytest
from datetime import datetime
from app.utils import format_date, validate_email, is_doctor_available
from app import db
from app.models import DoctorAvailability

# ---------- Utility Function Tests ----------

def test_format_date_valid():
    """Test for valid datetime formatting."""
    date_obj = datetime(2025, 5, 13, 10, 30, 0)
    formatted_date = format_date(date_obj)
    assert formatted_date == "2025-05-13 10:30:00", f"Expected '2025-05-13 10:30:00', but got {formatted_date}"

def test_format_date_invalid_input():
    """Test for invalid input (non-datetime)."""
    with pytest.raises(ValueError):
        format_date("2025-05-13")  # Pass a string instead of a datetime object

def test_validate_email_valid():
    """Test for valid email address."""
    email = "test@example.com"
    result = validate_email(email)
    assert result is True, "Valid email should return True"

def test_validate_email_invalid_missing_at():
    """Test for invalid email without '@' symbol."""
    email = "testexample.com"
    with pytest.raises(ValueError):
        validate_email(email)

def test_validate_email_invalid_missing_dot():
    """Test for invalid email without '.' symbol."""
    email = "test@com"
    with pytest.raises(ValueError):
        validate_email(email)

def test_is_doctor_available_valid_time(init_db):
    """Test for checking doctor's availability within the correct time frame."""
    doctor_id = 1
    start_time = datetime(2025, 4, 16, 10, 0)
    end_time = datetime(2025, 4, 16, 11, 0)
    
    # Add availability data
    availability = DoctorAvailability(
        doctor_id=doctor_id,
        available_from=datetime(2025, 4, 16, 9, 0),
        available_to=datetime(2025, 4, 16, 17, 0)
    )
    db.session.add(availability)
    db.session.commit()
    
    # Test if doctor is available
    result = is_doctor_available(doctor_id, start_time, end_time, db)
    assert result is True, "Doctor should be available during the specified time."

def test_is_doctor_available_invalid_time(init_db):
    """Test for checking doctor's availability when the time is outside available range."""
    doctor_id = 1
    start_time = datetime(2025, 4, 16, 18, 0)  # Time outside of availability
    end_time = datetime(2025, 4, 16, 19, 0)
    
    # Add availability data
    availability = DoctorAvailability(
        doctor_id=doctor_id,
        available_from=datetime(2025, 4, 16, 9, 0),
        available_to=datetime(2025, 4, 16, 17, 0)
    )
    db.session.add(availability)
    db.session.commit()
    
    # Test if doctor is not available
    result = is_doctor_available(doctor_id, start_time, end_time, db)
    assert result is False, "Doctor should not be available outside the specified time."
