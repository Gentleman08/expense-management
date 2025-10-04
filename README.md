# 💸 Expense Management

[![Repo size](https://img.shields.io/github/repo-size/Gentleman08/expense-management?style=flat-square)](https://github.com/Gentleman08/expense-management)
[![Last commit](https://img.shields.io/github/last-commit/Gentleman08/expense-management?style=flat-square)](https://github.com/Gentleman08/expense-management/commits/main)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)](https://www.python.org/)

This is a small Django-based expense management application with two main apps:

- `users` — custom user model, authentication and registration.
- `manager` — manager dashboard and expense approval flows.
- `core` — (added by Auth/Manager branches) shared core app for common models/views.

This repo contains a ready-to-run development project (SQLite database included) and Django apps for submitting and approving expenses.

## 🔍 Project structure (high level)

```
expense_management/
	├─ manage.py
	├─ db.sqlite3                      # development database (SQLite)
	├─ expense_management/             # Django project (settings, urls, wsgi/asgi)
	├─ manager/                         # manager app (dashboard, approvals)
	└─ users/                           # users app (custom user + auth)
	└─ templates/                       # HTML templates for views
```

## ✨ Features

- User registration and login
- Manager and admin dashboards
- Submit expense entries and view expense history
- Django admin integration

## 🚀 Quickstart (Windows - cmd.exe)

These commands assume you're on Windows (cmd.exe) and inside the repository root (`h:\expense-management`).

1. Create and activate a virtual environment

```batch
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies

If there is a `requirements.txt` in the project root, use it. If not, install Django (the project was built with Django):

```batch
pip install -r requirements.txt
# or if requirements.txt is not present
pip install Django
```

3. Apply migrations (database is included but running migrations is safe)

```batch
python manage.py migrate
```

4. Create a superuser (optional, for admin access)

```batch
python manage.py createsuperuser
```

5. Run the development server

```batch
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. The admin is typically at `/admin/`.

# expense-management
