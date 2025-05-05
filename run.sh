#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Apply migrations
python manage.py migrate

# Seed sample data (only if no tasks exist)
python manage.py seed_data

# Run the server with debug info
python manage.py runserver 0.0.0.0:8000 