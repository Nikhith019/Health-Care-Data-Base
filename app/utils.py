# utils.py
from datetime import datetime

def format_date(date_obj):
    """Formats a datetime object to a string."""
    if not isinstance(date_obj, datetime):
        raise ValueError("Input must be a datetime object")
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")

def validate_email(email):
    """Validates an email address."""
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address")
    return True

def is_doctor_available(doctor_id, start_time, end_time, db):
    """Check if the doctor is available in the provided time range."""
    availability = db.session.query(DoctorAvailability).filter(
        DoctorAvailability.doctor_id == doctor_id,
        DoctorAvailability.available_from <= start_time,
        DoctorAvailability.available_to >= end_time
    ).first()
    
    if availability:
        return True
    return False
