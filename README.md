# Quiz 3: Django Model-View-URL-Template Demo

This project shows the basic flow in Django:
Model → View → URL → Template

## What's inside

- `main/models.py` — the `Student` model
- `main/views.py` — the `home` view that fetches students
- `main/urls.py` — app-level URL that points to the `home` view
- `config/urls.py` — project-level URL that includes the app URLs
- `main/admin.py` — registers `Student` so you can add records in Django Admin
- `main/templates/main/home.html` — the page that displays the students
- `config/settings_snippet.py` — shows the one line to add to `settings.py`

## Setup from scratch

Run these commands in order, inside your `quiz3_django` folder.

### 1. Create and activate a virtual environment

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Django
```
pip install django
django-admin --version
```

### 3. Start the project
```
django-admin startproject config .
```

### 4. Create the app
```
python manage.py startapp main
```

### 5. Copy the files from this folder

Copy `models.py`, `views.py`, `urls.py`, and `admin.py` into your `main` folder.
Copy `config/urls.py` into your `config` folder.
Copy the `templates` folder into your `main` folder.

### 6. Update settings.py

Open `config/settings.py`. Add `'main',` to `INSTALLED_APPS`. See `settings_snippet.py` for the exact spot.

### 7. Create the database tables
```
python manage.py makemigrations
python manage.py migrate
```

### 8. Create a superuser (so you can log in to admin)
```
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### 9. Run the server
```
python manage.py runserver
```

Open the link in your terminal. It's usually `http://127.0.0.1:8000/`.

### 10. Add sample student records

Go to `http://127.0.0.1:8000/admin/`. Log in with your superuser account.
Click **Students**, then **Add Student**. Add at least 3 records.

Go back to `http://127.0.0.1:8000/` to see them listed on the home page.

## Push to GitHub

Create a file named `.gitignore` in your project root with this content:
```
venv/
__pycache__/
*.pyc
db.sqlite3
```

Then run:
```
git init
git add .
git commit -m "Quiz 3 Django MVT demo"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/quiz3-django.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Create the empty repo on GitHub first, named `quiz3-django`, before you push.

## Deploy on PythonAnywhere

1. Sign up at pythonanywhere.com.
2. Open a **Bash console** from your dashboard.
3. Clone your repo:
   ```
   git clone https://github.com/YOUR-USERNAME/quiz3-django.git
   ```
4. Go to the **Web** tab, click **Add a new web app**.
5. Choose **Manual configuration** and pick your Python version.
6. Set the **source code** path to your cloned project folder.
7. Open a console and create a virtual environment inside PythonAnywhere, then install Django in it:
   ```
   mkvirtualenv myenv --python=python3.10
   pip install django
   ```
8. On the Web tab, set the **virtualenv** path to point to `myenv`.
9. Edit the **WSGI configuration file** (link is on the Web tab) so it points to your `config` module, not the default example.
10. Run migrations from a Bash console inside your project folder:
    ```
    python manage.py migrate
    python manage.py createsuperuser
    ```
11. Click **Reload** on the Web tab.
12. Open your PythonAnywhere URL and test it. Add your sample students through `/admin/` if the database reset during deployment.

## Submission

Submit both links in Google Classroom in this format:
```
Name: [Your Full Name]
PythonAnywhere Link: [Your PythonAnywhere URL]
GitHub Link: [Your GitHub Repository URL]
```
