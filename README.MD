# NayePankh Volunteer Management Portal

A Django web application to manage volunteers for NayePankh Foundation.

## Features
- Login / Signup authentication
- Add, Edit, Delete volunteers
- Search by name, filter by skill and city
- Export filtered volunteers to CSV
- Dashboard with stats and charts
- Django Admin panel

## Tech Stack
- Python 3.10
- Django 5.2
- Bootstrap 5
- SQLite

## Setup Instructions

1. Clone the repo
   git clone https://github.com/yourusername/volunteer_portal.git
   cd volunteer_portal

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Create superuser
   python manage.py createsuperuser

6. Start server
   python manage.py runserver

7. Open http://127.0.0.1:8000