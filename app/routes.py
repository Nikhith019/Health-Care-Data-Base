from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import db
from .models import Patient, Doctor, Appointment, DoctorAvailability

main = Blueprint('main', __name__)

# ---------- API ROUTES ----------

@main.route('/')
def home():
    return render_template('login.html')  # Render the login page instead of JSON response


# Patient API Routes
@main.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    try:
        patient = Patient(
            name=data['name'],
            age=data['age'],
            gender=data['gender']
        )
        db.session.add(patient)
        db.session.commit()
        return jsonify({"message": "Patient created", "patient": patient.to_dict()}), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])

@main.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return jsonify(patient.to_dict())

@main.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = Patient.query.get_or_404(patient_id)
    patient.name = data.get('name', patient.name)
    patient.age = data.get('age', patient.age)
    patient.gender = data.get('gender', patient.gender)
    db.session.commit()
    return jsonify({"message": "Patient updated", "patient": patient.to_dict()})

@main.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted"})

# Doctor API Routes
@main.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()
    try:
        doctor = Doctor(name=data['name'], specialization=data['specialization'])
        db.session.add(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor created", "doctor": doctor.to_dict()}), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([doctor.to_dict() for doctor in doctors])

# Appointment API Routes
@main.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    try:
        appointment = Appointment(
            patient_id=data['patient_id'],
            doctor_id=data['doctor_id'],
            date=data['date'],
            notes=data.get('notes')
        )
        db.session.add(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment created", "appointment": appointment.to_dict()}), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments])


# ---------- FRONTEND FORM ROUTES (HTML) ----------

@main.route('/form/availability', methods=['GET', 'POST'])
def doctor_availability_form():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        available_from = request.form['available_from']
        available_to = request.form['available_to']

        new_availability = DoctorAvailability(
            doctor_id=doctor_id,
            available_from=available_from,
            available_to=available_to
        )
        db.session.add(new_availability)
        db.session.commit()
        return redirect(url_for('main.doctor_availability_form'))

    return render_template('availability_form.html')

@main.route('/form/patient', methods=['GET', 'POST'])
def patient_form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']

        new_patient = Patient(name=name, age=age, gender=gender)
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('main.patient_form'))

    return render_template('patient_form.html')

@main.route('/form/appointment', methods=['GET', 'POST'])
def appointment_form():
    patients = Patient.query.all()
    doctors = Doctor.query.all()

    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        date = request.form['date']
        notes = request.form['notes']

        new_appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            notes=notes
        )
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('main.appointment_form'))

    return render_template('appointment_form.html', patients=patients, doctors=doctors)

