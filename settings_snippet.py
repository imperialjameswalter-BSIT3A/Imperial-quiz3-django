# Add this to config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',  # <-- add this line
]

# TEMPLATES is already set up correctly by default.
# Django finds main/templates/main/home.html automatically
# because APP_DIRS is True in the default settings.py.
