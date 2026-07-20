# GitHub Setup Guide

## Step-by-Step Instructions

### 1. Create a GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `bugtracker`
3. Choose "Public" or "Private" (your choice)
4. **DO NOT** initialize with README, .gitignore, or license (we have these already)
5. Click "Create repository"

### 2. Push Your Code to GitHub

Open PowerShell in your project folder and run:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - bug tracker app"

# Add remote repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/bugtracker.git

# Rename branch to main and push
git branch -M main
git push -u origin main
```

### 3. Verify on GitHub

- Go to your repository: https://github.com/YOUR_USERNAME/bugtracker
- You should see all your code files
- You should NOT see:
  - `db.sqlite3` ✓ (excluded by .gitignore)
  - `.env` ✓ (excluded by .gitignore)
  - `venv/` ✓ (excluded by .gitignore)
  - `__pycache__/` ✓ (excluded by .gitignore)

### 4. Clone/Download on Another Computer

```bash
git clone https://github.com/YOUR_USERNAME/bugtracker.git
cd bugtracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
```

## Common Issues

### "fatal: not a git repository"
```bash
git init  # First time only
```

### Changes not showing on GitHub
```bash
git add .
git commit -m "Your message"
git push
```

### `.env` or `db.sqlite3` accidentally committed
```bash
git rm --cached db.sqlite3
git rm --cached .env
git commit -m "Remove sensitive files"
git push
```

## Next Steps

1. ✅ Push to GitHub
2. Choose a hosting platform (PythonAnywhere / Heroku / AWS)
3. See DEPLOYMENT.md for specific instructions
