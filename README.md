# 🎬 Cinema Reviews App

A Django-based movie management system where users can add, update, view, and delete movies. It also supports managing reviews for each movie with pagination, Bootstrap styling, and Material Icons integration.

Features
CRUD operations for movies and reviews:
Create, update, and delete movies and reviews.
Pagination: Easily browse through multiple movies.
Material Icons: Styled icons for actions like editing and deleting.
Bootstrap Integration for responsive design.
Authentication: Add, update, and delete actions require login.
Prerequisites
Python 3.x
Django 4.x
Bootstrap 5 (CDN)
Material Icons (Google Fonts)
Installation
Clone the repository:

bash
Copiar código
git clone https://github.com/Srdonas/Django-CinemaReviews.git
cd cinema-reviews-app
Create a virtual environment (recommended):

bash
Copiar código
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
Install dependencies:

bash
Copiar código
pip install -r requirements.txt
Apply migrations to set up the database:

bash
Copiar código
python manage.py migrate
Create a superuser (for admin access):

bash
Copiar código
python manage.py createsuperuser
Run the development server:

bash
Copiar código
python manage.py runserver
Configuration for Global Templates and Static Files
Ensure your Django settings are configured correctly for global templates and static directories.

In your settings.py, you should have something like this:

python
Copiar código
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Global template directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Global templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Global static files directory
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Global static directory
]
Directory Structure Example:

csharp
Copiar código
cinema-reviews-app/
│
├── static/             # Global static files (CSS, JS, Images)
│   └── css/
│       └── base.css
│
├── templates/          # Global templates
│   ├── base.html
│   └── movies/
│       ├── movie_list.html
│       ├── movie_detail.html
│       ├── update_movie.html
│       └── create_review.html
│
├── movies/             # Django app folder
│   ├── migrations/     # Database migrations
│   ├── views.py        # Application logic
│   ├── models.py       # Database models
│   ├── urls.py         # URL routing
│   └── forms.py        # Forms for movie and review models
│
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # Documentation (this file)

Usage
Access the app:
Visit http://127.0.0.1:8000 in your browser.

Login:
Use the admin credentials to access all features (add, edit, delete movies and reviews).

Features:

View movies: Click on the movie cards to see the details and reviews.
Add new movies: Use the "Add a new movie" button after logging in.
Edit or delete movies: Use the "Edit" and "Delete" buttons on each movie card.
Pagination: Navigate between pages using pagination controls.
Technologies Used
Backend: Django 4.x
Frontend: HTML, CSS, Bootstrap 5, Material Icons
Database: SQLite (default for Django)
To Do
Implement AJAX for smooth delete operations without reloading the page.
Add unit tests for the CRUD operations.
Improve styling with more advanced Bootstrap components.