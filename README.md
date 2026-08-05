# 📚 Library Management System

A full-stack web application built with **Django** that enables library members to browse books, borrow available copies, return borrowed books, and manage their active loans. The project also provides an administrative interface for librarians using Django Admin to manage the catalog and monitor loan records.

This project was developed as a team-based academic project following the Software Requirements Specification (SRS), focusing on Django's MVT architecture, authentication, database relationships, and business logic.

---

## Prerequisites

- Python 3.12 or newer
- Git
- GitHub CLI (`gh`) for repository and pull request workflow
- SQLite, included with Python, for local development
- A virtual environment created with `python -m venv`

---

# ✨ Features

## 👤 Authentication

* User registration
* Secure login & logout
* Password hashing using Django Authentication
* Form validation

---

## 📖 Book Catalog

* Browse all available books
* Search books by title or author
* View book details
* Display available books

---

## 📚 Borrow & Return System

* Borrow books when copies are available
* Prevent borrowing unavailable books
* Prevent borrowing the same book twice simultaneously
* Return borrowed books

---

## 📋 My Loans

* View all currently borrowed books
* Track borrowing status
* Return books 

---

## 🔧 Admin Panel

Powered by Django Admin.

Administrators can:

* Add books
* Edit books
* Delete books
* Manage categories
* Monitor active loans
* Manage users

---

# 🛠️ Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite

### Authentication

* Django Authentication System

---

# 🗂️ Project Structure

```text
library_management/
│
├── accounts/
│   ├── authentication
│   ├── signup
│   └── login
│
├── catalog/
│   ├── books
│   ├── categories
│   └── search
│
├── loans/
│   ├── borrow
│   ├── return
│   └── my loans
│
├── templates/
├── static/
├── media/
└── manage.py
```

---

# 🗃️ Database Design

## User

Uses Django's built-in User model.

---

## Book

* Title
* Author
* ISBN
* Category
* Total Copies
* Available Copies

---

## Loan

* Member
* Book
* Borrow Date
* Return Date
* Status

---

# 🔄 Application Workflow

```text
User Registration
        │
        ▼
      Login
        │
        ▼
 Browse Catalog
        │
        ▼
 Search Books
        │
        ▼
 Borrow Book
        │
        ▼
 Loan Created
        │
        ▼
 Available Copies Updated
        │
        ▼
 View My Loans
        │
        ▼
 Return Book
        │
        ▼
 Available Copies Increased
```

---

# 🔐 Business Rules

* Only authenticated users can borrow books.
* Books cannot be borrowed if no copies are available.
* A user cannot borrow the same book twice before returning it.
* Returning a book immediately updates the available copies.
* Passwords are securely hashed using Django Authentication.
* Only administrators have access to Django Admin.

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/AmirMustafa10/library-management-system.git
cd library-management-system
```

## Create virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Apply migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run the server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```


---


# 🤝 Team

Developed as part of a collaborative academic project using Git and GitHub workflow.
* Amir Mostafa
* Mohamed Osama 
* AbdElrhman Mohamed
* Sarah Maged
* Mina Mary 
* Merolla Mehab 

---

# 📄 License

This project is intended for educational purposes.

