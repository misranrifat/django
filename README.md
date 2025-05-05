# Django RESTful API Demo

A simple Django REST framework project demonstrating CRUD operations with SQLite database.

## Project Structure

```
django-restful/
├── api/                    # API app
│   ├── management/         # Custom management commands
│   │   └── commands/       # Command implementations
│   │       └── seed_data.py# Data seeding command
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Admin site configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Data models
│   ├── serializers.py      # API serializers
│   ├── services.py         # Business logic layer
│   ├── urls.py             # API URL routing
│   └── views.py            # API views and logic
├── core/                   # Project settings
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── venv/                   # Virtual environment
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
├── README.md               # Project documentation
└── run.sh                  # Startup script
```

## Features

- RESTful API with Django Rest Framework
- CRUD operations for Task management
- SQLite database for persistence
- Browsable API interface
- Seed data command for quick setup

## Setup and Running

### Prerequisites

- Python 3.8+
- Pip package manager

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-restful.git
   cd django-restful
   ```

2. Create a virtual environment and install dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install django djangorestframework
   ```

3. Run the application:
   ```
   ./run.sh
   ```

The server will be available at http://localhost:8000/

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/v1/tasks/ | List all tasks |
| POST   | /api/v1/tasks/ | Create a new task |
| GET    | /api/v1/tasks/{id}/ | Retrieve a task |
| PUT    | /api/v1/tasks/{id}/ | Update a task |
| PATCH  | /api/v1/tasks/{id}/ | Partially update a task |
| DELETE | /api/v1/tasks/{id}/ | Delete a task |

### Business Logic Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/v1/tasks/completed/ | List all completed tasks |
| GET    | /api/v1/tasks/pending/ | List all pending tasks |
| GET    | /api/v1/tasks/overdue/?days=7 | List tasks that are overdue (pending for more than X days) |
| GET    | /api/v1/tasks/statistics/ | Get task statistics (counts, completion rate) |
| POST   | /api/v1/tasks/{id}/mark_completed/ | Mark a task as completed |
| POST   | /api/v1/tasks/{id}/mark_pending/ | Mark a task as pending |
| DELETE | /api/v1/tasks/delete_all/ | Delete all tasks |

## Data Model

### Task
- `title` (string): Task title (required)
- `description` (string): Task details (optional)
- `completed` (boolean): Task completion status
- `created_at` (datetime): Creation timestamp
- `updated_at` (datetime): Last modification timestamp

## Example API Usage

### List all tasks
```bash
curl -X GET http://localhost:8000/api/v1/tasks/
```

### Create a task
```bash
curl -X POST http://localhost:8000/api/v1/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "description": "Details about the task", "completed": false}'
```

### Retrieve a task
```bash
curl -X GET http://localhost:8000/api/v1/tasks/1/
```

### Update a task
```bash
curl -X PUT http://localhost:8000/api/v1/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Task", "description": "Updated details", "completed": true}'
```

### Delete a task
```bash
curl -X DELETE http://localhost:8000/api/v1/tasks/1/
```

### Business Logic Examples

```bash
# Get only completed tasks
curl -X GET http://localhost:8000/api/v1/tasks/completed/

# Get task statistics
curl -X GET http://localhost:8000/api/v1/tasks/statistics/

# Mark a task as completed
curl -X POST http://localhost:8000/api/v1/tasks/1/mark_completed/

# Get overdue tasks (pending for more than 10 days)
curl -X GET http://localhost:8000/api/v1/tasks/overdue/?days=10

# Delete all tasks
curl -X DELETE http://localhost:8000/api/v1/tasks/delete_all/
```

## Notes

- This project uses a SQLite database for simplicity, which persists data between restarts.
- The seed_data command populates the database with sample tasks only if no tasks exist.