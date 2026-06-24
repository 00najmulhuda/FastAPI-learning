# FastAPI Learning Journey 🚀

A hands-on FastAPI backend learning repository where I build real-world backend features step by step, from basic APIs to authentication, authorization, database relationships, and production-ready backend concepts.

## 📌 About This Repository

This repository documents my backend development journey using FastAPI and PostgreSQL. Instead of only learning theory, every concept is implemented through practical projects and API development.

Current focus:

* FastAPI
* PostgreSQL
* SQLModel ORM
* JWT Authentication
* REST APIs
* Database Relationships
* Backend Architecture
* API Testing with Postman

---

## 🛠 Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLModel
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)
* Uvicorn
* Postman
* Git & GitHub

---

## ✅ Features Implemented

### Authentication System

* User Registration
* Password Hashing using bcrypt
* Secure Login System
* JWT Access Token Generation
* Token Verification
* Protected Routes
* Current User (/me) Endpoint

### Database

* PostgreSQL Integration
* SQLModel ORM
* Session Management
* Database Relationships
* CRUD Operations

### API Development

* GET Endpoints
* POST Endpoints
* PUT Endpoints
* DELETE Endpoints
* Request Validation
* Response Handling
* Error Handling

---

## 🔐 Authentication Flow

User Register
↓
Password Hashed (bcrypt)
↓
Stored in PostgreSQL
↓
User Login
↓
JWT Access Token Generated
↓
Protected Route Access
↓
Current User Information Retrieved

---

## 📂 Project Structure

```bash
FastAPI-learning/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── auth_routes.py
├── auth_models.py
├── auth_schemas.py
│
├── requirements.txt
└── README.md
```

## 🚀 Running Locally

### Clone Repository

```bash
git clone https://github.com/00najmulhuda/FastAPI-learning.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn main:app --reload
```

### Open API Docs

```bash
http://127.0.0.1:8000/docs
```

---

## 📸 Screenshots

Add:

* Swagger UI
* User Registration
* Login API
* JWT Token Response
* Protected Route Access
* /me Endpoint Response
* Postman Testing

---

## 🎯 Learning Goals

* Build production-ready backend systems
* Understand authentication and authorization
* Master FastAPI ecosystem
* Learn database design and relationships
* Prepare for backend internships and full-stack roles

---

## 📈 Current Progress

✔ CRUD APIs

✔ PostgreSQL Integration

✔ SQLModel ORM

✔ Database Relationships

✔ JWT Authentication

✔ User Registration

✔ User Login

✔ Protected Routes

✔ Current User Endpoint

🔄 Role-Based Access Control (RBAC)

🔄 File Upload

🔄 Email Integration

🔄 Deployment

---

## 👨‍💻 Author

**Najmul Huda**

GitHub: https://github.com/00najmulhuda

Building real-world backend systems while learning FastAPI and modern web development.
