# FastAPI RBAC - Role-Based Access Control

## 📌 Project Description

This project implements a Role-Based Access Control (RBAC) and permission-based authorization system using FastAPI and PostgreSQL.

The system allows users to access specific API operations based on their assigned roles and permissions.

## 🎯 Objective

The main objective is to move beyond basic authentication and implement production-style authorization with centralized permission management.

## 🛠️ Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Pydantic
- Uvicorn

## 🔐 Features

- User authentication
- Role-based access control
- Permission-based authorization
- Role and permission management
- Protected API routes
- Centralized authorization logic
- Least privilege access
- PostgreSQL database integration

## 👥 Roles

Example roles include:

- Admin
- Manager
- User

## 🔑 Permissions

Example permissions:

- user:read
- user:create
- user:update
- user:delete

## 📂 Project Structure

```text
fastapi-rbac/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── auth/
│   │   ├── authentication.py
│   │   └── authorization.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   └── users.py
│   │
│   └── dependencies.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md+
