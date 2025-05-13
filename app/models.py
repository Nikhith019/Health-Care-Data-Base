from app import db

class DoctorAvailability(db.Model):
    __tablename__ = 'doctor_availability'
    
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', name='fk_doctor_availability_doctor_id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    is_booked = db.Column(db.Boolean, default=False, nullable=False)
    
    doctor = db.relationship('Doctor', back_populates='availabilities')
    appointments = db.relationship('Appointment', back_populates='availability')

class Doctor(db.Model):
    __tablename__ = 'doctor'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    speciality = db.Column(db.String(100), nullable=False)
    
    availabilities = db.relationship('DoctorAvailability', back_populates='doctor', cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', back_populates='doctor')

class Appointment(db.Model):
    __tablename__ = 'appointment'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', name='fk_appointment_patient_id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id', name='fk_appointment_doctor_id'), nullable=False)
    availability_id = db.Column(db.Integer, db.ForeignKey('doctor_availability.id', name='fk_appointment_availability_id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    
    patient = db.relationship('Patient', back_populates='appointments')
    doctor = db.relationship('Doctor', back_populates='appointments')
    availability = db.relationship('DoctorAvailability', back_populates='appointments')

class Patient(db.Model):
    __tablename__ = 'patient'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    appointments = db.relationship('Appointment', back_populates='patient', cascade='all, delete-orphan')

class Medication(db.Model):
    __tablename__ = 'medication'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', name='fk_medication_patient_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    
    patient = db.relationship('Patient', back_populates='medications')

class MedicalRecord(db.Model):
    __tablename__ = 'medical_record'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id', name='fk_medical_record_patient_id'), nullable=False)
    record_date = db.Column(db.DateTime, nullable=False)
    record_details = db.Column(db.Text, nullable=False)
    
    patient = db.relationship('Patient', back_populates='medical_records')
