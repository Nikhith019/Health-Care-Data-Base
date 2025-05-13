Healthcare Database Management System (DBMS)

Project Overview

The Healthcare Database Management System (DBMS) is a software system designed to manage and store healthcare data, including patient records, medical histories, appointments, prescriptions, and more. This system helps medical staff, administrators, and patients easily manage and retrieve important medical information, improving the overall workflow of healthcare operations.

The DBMS enables healthcare institutions to store and access patient data securely and efficiently, providing support for daily administrative and medical tasks. It offers a reliable system for managing sensitive information while ensuring compliance with health regulations and standards.

Features

Patient Management
Store patient details: personal info, medical history, appointments, and treatments.
Track and manage diseases, treatments, and ongoing medications.
Staff Management
Manage doctor and nurse profiles with their specializations, shifts, and departments.
Assign roles and responsibilities for better coordination.
Appointment Scheduling
Book, update, or cancel patient appointments.
Assign appointments with the appropriate medical staff and track appointment status.
Prescription Management
Record patient prescriptions and track medication usage.
Monitor medication supply levels for the pharmacy.
Reporting & Analytics
Generate and download reports for appointments, diagnoses, treatments, etc.
Provide insights into patient history, treatment outcomes, and department efficiency.
Technologies Used

Database: MySQL / PostgreSQL
Backend: Python (Flask/Django for API services), Java (Spring Boot)
Frontend: HTML, CSS, JavaScript (React.js for dynamic UI)
ORM: SQLAlchemy (Python), Hibernate (Java)
Authentication: JWT (JSON Web Token) for user authentication
Deployment: Docker (for containerized app), AWS/Heroku (for cloud hosting)
Database Schema

The system uses several key tables to organize and manage healthcare data:

1. Patients
Stores essential patient information.

patient_id (INT, Primary Key)
name (VARCHAR)
dob (DATE)
gender (VARCHAR)
contact_info (VARCHAR)
medical_history (TEXT)
2. Doctors
Stores information about healthcare professionals.

doctor_id (INT, Primary Key)
name (VARCHAR)
specialization (VARCHAR)
contact_info (VARCHAR)
department (VARCHAR)
3. Appointments
Tracks patient appointments with medical professionals.

appointment_id (INT, Primary Key)
patient_id (INT, Foreign Key)
doctor_id (INT, Foreign Key)
appointment_date (DATETIME)
status (VARCHAR) (Scheduled, Completed, Cancelled)
4. Prescriptions
Stores prescriptions for patients, including medication details.

prescription_id (INT, Primary Key)
patient_id (INT, Foreign Key)
medication_name (VARCHAR)
dosage (VARCHAR)
prescribed_by (INT, Foreign Key)
start_date (DATE)
end_date (DATE)
5. Staff
Contains data for medical and non-medical staff.

staff_id (INT, Primary Key)
name (VARCHAR)
role (VARCHAR)
department (VARCHAR)
contact_info (VARCHAR)
shift (VARCHAR)
