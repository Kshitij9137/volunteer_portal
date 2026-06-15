# Volunteer Management Portal

A Django web application built for NayePankh Foundation to manage and track volunteers.

🔗 Live Demo: https://nayepankh-volunteer-portal-sygk.onrender.com

---

## Features

- Login, signup and logout authentication
- Add, edit, view and delete volunteers
- Search by name, filter by skill and city
- Export volunteer data to CSV
- Dashboard with volunteer statistics
- Django admin panel for superusers
- Fully responsive with Bootstrap 5

---

## Tech Stack

- Python 3.10
- Django 5.2
- Bootstrap 5
- SQLite (local) / PostgreSQL (production)
- Deployed on Render

---

## Local Setup

1. Clone the repository
```
git clone https://github.com/Kshitij9137/volunteer_portal.git
cd volunteer_portal
```

2. Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run migrations
```
python manage.py migrate
```

5. Create superuser
```
python manage.py createsuperuser
```

6. Start the server
```
python manage.py runserver
```

7. Open http://127.0.0.1:8000 in your browser

---

## Project Structure

```
volunteer_portal/
├── volunteer_portal/     # Project settings and URLs
├── volunteers/           # Main app (models, views, forms, URLs)
├── templates/            # HTML templates
├── static/               # Static files
├── build.sh              # Render build script
├── requirements.txt
└── README.md
```

---

## Deployment

Deployed on Render (free tier).
Live URL: https://your-app-name.onrender.com

Note: Free tier spins down after 15 minutes of inactivity.
First request may take 30-60 seconds to wake up.

---

## Author

Your Name
GitHub: https://github.com/Kshitij9137

---

Built as part of the NayePankh Foundation Python Development Internship.