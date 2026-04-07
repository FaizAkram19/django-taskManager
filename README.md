# Task Manager

A Django-based task management application built for learning and productivity.

## Features

- **Create, Read, Update, Delete Tasks** — Full CRUD operations
- **Task Priorities** — Assign priority levels to tasks
- **Mark Complete** — Track task completion status
- **Due Dates** — Set and manage task deadlines
- **Deadline Notifications** — Visual warnings when deadlines are approaching
- **Published Date Tracking** — Automatic timestamp on task creation

## Tech Stack

- Django 4.x
- SQLite (default)
- HTML/CSS Forms

## Setup

### Prerequisites
- Python 3.8+
- pip
- git

### Installation

```bash
git clone <repo-url>
cd task-manager
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django
```

### Initial Setup

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to start.

## Project Structure

```
task-manager/
├── manage.py
├── task_manager/          # Project settings
├── tasks/                 # App
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
└── README.md
```

## Learning Goals

This project focuses on:
- Django models and migrations
- Class-based views
- Django forms
- Templates and template logic
- URL routing
- Admin customization

## Status

🚀 MVP in development