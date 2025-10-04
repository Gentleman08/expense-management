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

## 🗄️ Database notes

- The repository includes `db.sqlite3` for convenience. This is fine for local development but do not use it for production.
- If you want a clean DB, remove `db.sqlite3` and re-run `python manage.py migrate`.

## 🧪 Running tests

```batch
python manage.py test
```

## 🧰 Development notes

- Templates live under `expense_management/templates`.
- App code for users and manager is in `users/` and `manager/` respectively.
- Project settings are in `expense_management/expense_management/settings.py`.

If you add environment-specific settings (secret keys, DB credentials), keep them out of version control and use environment variables or a separate config file.

## 🔧 Common issues & troubleshooting

- Merge conflicts / unfinished merges: If you see "You have unmerged paths" or an unfinished merge, run:

```batch
git merge --abort
# or, if you stashed changes before switching branches
git stash list
git stash apply
```

- Permission errors running server on Windows: try a different port

```batch
python manage.py runserver 8001
```

## 🧾 Contributing

1. Create a branch with a descriptive name (for example `feature/auth-fixes`).
2. Make small, focused commits.
3. Open a pull request against `main` and add a description of what you changed.

If you'd like, I can help create a `requirements.txt`, add CI badges, or clean up generated `__pycache__` and the `db.sqlite3` before publishing.

## 📞 Contact / Next steps

- If you'd like the README to include screenshots or custom icons (SVG/PNG), tell me where to place them and I can add them to the repo and wire them into the README.
- I can also:
  - generate a `requirements.txt` from the environment,
  - add a `.gitignore` tuned for Django (if missing),
  - remove committed bytecode files and add `.gitignore` entries.

---

Made with ❤️ — update this README if you rename apps or change the project layout.

# expense-management
