# Library Management System

A Django-based Library Management System built from the provided SRS. The merged baseline includes Task #2, and this branch implements Task #4: front-end templates and CSS.

## Prerequisites

- Python 3.12 or newer
- Git
- GitHub CLI (`gh`) for repository and pull request workflow
- SQLite, included with Python, for local development
- A virtual environment created with `python -m venv`

## Setup

```bash
git clone https://github.com/magedhara251-bot/library-management-system.git
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

Open the app at:

- Catalog: http://127.0.0.1:8000/
- My Loans placeholder page: http://127.0.0.1:8000/loans/my/
- Django Admin: http://127.0.0.1:8000/admin/

## Implemented Scope

Implemented:

- Clean Django project scaffold with `accounts`, `catalog`, and `loans` apps.
- `Book` model with title, author, ISBN, category, total copies, and available copies.
- Model validation and database constraints to prevent invalid copy counts.
- Django Admin registration for catalog management.
- Sample book seed command.
- Base template and navigation.
- Catalog page template with styled book cards.
- My Loans page template with placeholder data until FR-3 is implemented.
- Shared CSS for layout, cards, tables, and responsive behavior.

Not implemented in this branch:

- Authentication views and templates.
- Borrowing and returning logic.
- JavaScript filtering.
- Custom librarian dashboard.

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_books
python manage.py test
python manage.py runserver
```
