# Library Management System

A Django-based Library Management System built from the provided SRS. This branch implements Task #2: Backend Models & Admin for the Book Catalog (FR-2).

## Prerequisites

- Python 3.12 or newer
- Git
- GitHub CLI (`gh`) for repository and pull request workflow
- SQLite, included with Python, for local development
- A virtual environment created with `python -m venv`

## Setup

```bash
git clone https://github.com/ESLAMAHMED232/library-management-system.git
cd library-management-system
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py seed_books
python manage.py createsuperuser
python manage.py runserver
```

On macOS or Linux, activate the virtual environment with:

```bash
source .venv/bin/activate
```

## Task #2 Scope

Implemented:

- Clean Django project scaffold with `accounts`, `catalog`, and `loans` apps.
- `Book` model with title, author, ISBN, category, total copies, and available copies.
- Model validation and database constraints to prevent invalid copy counts.
- Django Admin registration for catalog management.
- Sample book seed command.

Not implemented in this branch:

- Authentication views and templates.
- Borrowing and returning logic.
- Catalog templates, CSS, or JavaScript filtering.
- Custom librarian dashboard.

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_books
python manage.py test
python manage.py runserver
```
