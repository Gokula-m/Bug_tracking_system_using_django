# Bugtracker - Django Bug Management System

A simple Django application for tracking and managing bugs.

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/bugtracker.git
   cd bugtracker
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or on Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   copy .env.example .env  # Windows
   # or on Mac/Linux:
   cp .env.example .env
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Visit: http://localhost:8000

## 📋 Database

**Local Development:** SQLite (included)
**Production:** PostgreSQL recommended

Your `.gitignore` excludes:
- `db.sqlite3` - Database file (never committed to GitHub)
- `.env` - Local environment variables (never committed to GitHub)

## 🌐 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions for:
- PythonAnywhere
- Heroku
- AWS / DigitalOcean
- Generic VPS

### Key Points:

✅ **DO commit to GitHub:**
- Python code
- Templates
- Static files
- `requirements.txt`
- `.env.example`

❌ **DO NOT commit to GitHub:**
- `.env` (secrets)
- `db.sqlite3` (database)
- `venv/` (virtual environment)
- `__pycache__/` (compiled files)

## 🔒 Security Notes

1. **Secret Key** - Changed to environment variable (`.env`)
2. **DEBUG Mode** - Controlled via environment variable
3. **ALLOWED_HOSTS** - Configure per environment
4. **Database** - Use PostgreSQL in production, SQLite locally

## 📦 Project Structure

```
bugtracker/
├── bugs/                 # Django app
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── bugtracker/          # Project config
│   ├── settings.py      # Configuration (uses environment variables)
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3          # Local database (not in GitHub)
├── manage.py
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Files to exclude from Git
└── DEPLOYMENT.md       # Deployment guide
```

## 🛠️ Technologies

- Django 6.0.5
- Python 3.9+
- SQLite (development) / PostgreSQL (production)

## 📝 License

[Your License Here]

## 👤 Author

[Your Name]
