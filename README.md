Healthcare Database Management System (DBMS)

Project Overview

The Healthcare Database Management System (DBMS) is a software solution designed to efficiently manage medical records, patient information, appointments, staff details, and medical history in a healthcare setting. It helps healthcare professionals, administrators, and patients interact seamlessly, streamlining tasks such as data storage, retrieval, and reporting.

This system aims to provide an organized, accessible, and secure database for managing patient records, appointments, medications, and treatments.

Features

Patient Management
Store and manage patient personal details (name, age, gender, etc.)
Track patient medical history, including diseases, treatments, and medications.
Staff Management
Manage details of doctors, nurses, and other medical staff.
Assign roles, shifts, and departments.
Appointment Scheduling
Book and manage appointments for patients.
Allow patients to schedule, cancel, or reschedule appointments.
Medical Records Management
Maintain detailed medical records for patients.
Record diagnoses, treatments, and follow-ups.
Pharmacy Management
Track and manage medication stock.
Record prescriptions and the dispensing of drugs.
Reporting
Generate reports for appointments, treatments, medication usage, etc.
Analytics on patient history, doctor visits, and more.
Technologies Used

Database: MySQL / PostgreSQL / SQLite (You can choose based on your requirements)
Backend: Python (Flask/Django for API services) or Java (Spring Boot)
Frontend: HTML, CSS, JavaScript, React.js (Optional for advanced UI)
ORM: SQLAlchemy (if using Python), Hibernate (if using Java)
Authentication: JWT (JSON Web Token) for secure user login
Deployment: Docker (for containerized deployment), AWS, Heroku, or any cloud-based service.
Database Schema

The Healthcare DBMS includes several tables, such as:

Patients
Stores patient details like name, address, date of birth, contact, and medical history.
patient_id (INT, Primary Key)
name (VARCHAR)
dob (DATE)
gender (VARCHAR)
contact_info (VARCHAR)
medical_history (TEXT)
Doctors
Stores doctor details, including name, specialization, contact, and assigned department.
doctor_id (INT, Primary Key)
name (VARCHAR)
specialization (VARCHAR)
contact_info (VARCHAR)
department (VARCHAR)
Appointments
Stores appointment details, linking patients with doctors and the appointment time.
appointment_id (INT, Primary Key)
patient_id (INT, Foreign Key)
doctor_id (INT, Foreign Key)
appointment_date (DATETIME)
status (VARCHAR) (Scheduled, Cancelled, Completed)
Medications
Stores medication details prescribed to patients.
medication_id (INT, Primary Key)
patient_id (INT, Foreign Key)
medication_name (VARCHAR)
dose (VARCHAR)
prescribed_by (INT, Foreign Key)
start_date (DATE)
end_date (DATE)
Staff
Details about medical and non-medical staff.
staff_id (INT, Primary Key)
name (VARCHAR)
role (VARCHAR)
department (VARCHAR)
contact_info (VARCHAR)
shift (VARCHAR)
