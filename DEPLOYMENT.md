# Bugtracker Django - GitHub & Deployment Guide

## Step 1: Prepare Your GitHub Repository

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit"

# Create repository on GitHub (github.com)
# Then:
git remote add origin https://github.com/YOUR_USERNAME/bugtracker.git
git branch -M main
git push -u origin main
```

## Step 2: Local Development Setup

```bash
# Create .env file from .env.example
cp .env.example .env

# Update .env with your local settings
# Make sure to generate a new SECRET_KEY for production

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Step 3: Choose Deployment Option

### Option A: PythonAnywhere (Easiest for beginners)
1. Sign up at https://www.pythonanywhere.com
2. Upload your code
3. Configure web app with your domain
4. SQLite works fine here

### Option B: Heroku
1. Sign up at https://www.heroku.com
2. Install Heroku CLI
3. Use PostgreSQL add-on
4. Push code with `git push heroku main`

### Option C: AWS / DigitalOcean
1. Create server instance
2. Install Python, PostgreSQL
3. Clone from GitHub
4. Use Gunicorn + Nginx + PostgreSQL

## Step 4: Update for Production

### Before Deploying:
1. Generate new SECRET_KEY
2. Set DEBUG=False
3. Add your domain to ALLOWED_HOSTS
4. Use PostgreSQL instead of SQLite
5. Set up environment variables on the hosting platform

### Generate New SECRET_KEY:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Database Note

**SQLite is fine for:**
- Local development
- Small projects with light traffic
- Learning Django

**Use PostgreSQL for:**
- Production
- Multiple concurrent users
- Cloud hosting

## Important Files Not in Git

Your `.gitignore` already excludes:
- `db.sqlite3` (database)
- `.env` (secrets)
- `__pycache__/` (compiled Python)
- `.venv/` (virtual environment)

## What Goes to GitHub

- All Python code
- Templates, static files
- `requirements.txt`
- `.env.example` (NEVER .env itself)
- This deployment guide

## First Time Deployment Checklist

- [ ] Generate new SECRET_KEY
- [ ] Create `.env` on server with production values
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Run `python manage.py migrate` on server
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Create admin user on production
