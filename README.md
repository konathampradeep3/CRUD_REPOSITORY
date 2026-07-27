# 🏥 Healthcare Backend API

A secure and scalable Healthcare Backend application built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**. This project provides RESTful APIs for user authentication, patient management, doctor management, and patient-doctor mapping using JWT authentication.

---

## 📌 Project Overview

This project was developed as part of a Django backend assignment to demonstrate the implementation of a secure healthcare management system.

The application allows users to:

- Register and log in using JWT authentication
- Manage patient records
- Manage doctor records
- Assign doctors to patients
- Perform CRUD operations through REST APIs
- Store data securely in PostgreSQL

---

## 🚀 Features

- User Registration
- User Login with JWT Authentication
- Patient CRUD Operations
- Doctor CRUD Operations
- Patient-Doctor Mapping
- Django REST Framework APIs
- PostgreSQL Database
- Django ORM
- Input Validation
- Authentication & Permissions
- Environment Variable Support
- RESTful API Design

---

## 🛠️ Technology Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- PostgreSQL

### Authentication
- JWT Authentication
- djangorestframework-simplejwt

### Deployment
- Render (Recommended)

### API Testing
- Postman

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
Healthcare-Backend/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│
├── healthcare/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── CRUD/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

## 🗄️ Database Models

### User
- Django Authentication User Model

### Patient

- Name
- Age
- Gender
- Phone Number
- Address
- Created By

### Doctor

- Name
- Specialization
- Email
- Phone Number
- Experience

### PatientDoctorMapping

- Patient
- Doctor
- Assigned Date

---

## 🔐 Authentication APIs

### Register

```
POST /api/auth/register/
```

Request

```json
{
    "username":"pradeep",
    "email":"pradeep@gmail.com",
    "password":"Password@123"
}
```

---

### Login

```
POST /api/auth/login/
```

Request

```json
{
    "username":"pradeep",
    "password":"Password@123"
}
```

Response

```json
{
    "refresh":"JWT Refresh Token",
    "access":"JWT Access Token"
}
```

---

## 👨‍⚕️ Patient APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/patients/ | Create Patient |
| GET | /api/patients/ | Get All Patients |
| GET | /api/patients/{id}/ | Get Patient |
| PUT | /api/patients/{id}/ | Update Patient |
| DELETE | /api/patients/{id}/ | Delete Patient |

---

## 👨‍⚕️ Doctor APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/doctors/ | Create Doctor |
| GET | /api/doctors/ | Get All Doctors |
| GET | /api/doctors/{id}/ | Get Doctor |
| PUT | /api/doctors/{id}/ | Update Doctor |
| DELETE | /api/doctors/{id}/ | Delete Doctor |

---

## 🔗 Patient Doctor Mapping APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/mappings/ | Assign Doctor |
| GET | /api/mappings/ | View All Mappings |
| GET | /api/mappings/{patient_id}/ | View Patient Mapping |
| DELETE | /api/mappings/{id}/ | Remove Mapping |

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/CRUD_REPOSITORY.git
```

Move into project

```bash
cd CRUD_REPOSITORY
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

---

## 🧪 Testing APIs

The APIs were tested using:

- Postman
- Django Admin
- PostgreSQL Database

---

## 🔒 Security Features

- JWT Authentication
- Protected API Endpoints
- Django ORM
- Input Validation
- Authentication Permissions
- Environment Variables

---

## 📷 Sample Workflow

1. Register User
2. Login
3. Copy JWT Access Token
4. Authorize Requests
5. Create Doctor
6. Create Patient
7. Assign Doctor to Patient
8. Retrieve Patient Information
9. Update Records
10. Delete Records

---

## 📈 Future Enhancements

- Appointment Scheduling
- Medical History Management
- Prescription Management
- File Upload Support
- Email Notifications
- Role-Based Access Control
- Swagger/OpenAPI Documentation
- Docker Deployment
- CI/CD Pipeline

---

## 👨‍💻 Author

**Konatham Pradeep**

Python Full Stack Developer

GitHub: https://github.com/konathampradeep3

---

## 📄 License

This project is created for educational purposes and technical assessment demonstrations.
