# Deploy to Render.com - Step by Step Guide

## Why Render?
- ✅ FREE tier available
- ✅ PostgreSQL database included
- ✅ Very beginner-friendly
- ✅ Auto-deploys from GitHub
- ✅ Perfect for Django apps

---

## Step 1: Push Code to GitHub

First, make sure your code is on GitHub (see GITHUB_SETUP.md):

```bash
git add .
git commit -m "Ready for deployment"
git push
```

Verify these files are on GitHub:
- ✅ `Procfile`
- ✅ `runtime.txt`
- ✅ `requirements.txt`
- ✅ `bugtracker/settings.py`
- ❌ `.env` (should NOT be there)
- ❌ `db.sqlite3` (should NOT be there)

---

## Step 2: Create PostgreSQL Database on Render

1. Go to https://render.com and **Sign Up** (free account)

2. Click **"New"** → **"PostgreSQL"**

3. Fill in:
   - **Name:** `bugtracker-db`
   - **Database:** `bugtracker_db`
   - **User:** `postgres` --> postgre(default)
   - **Region:** Closest to you
   - **PostgreSQL Version:** 15 (or latest)

4. Click **Create Database**

5. **Wait 2-3 minutes** for database to be ready

6. Copy the **Internal Database URL** (you'll need this!)
   - Should look like: `postgresql://username:password@host:5432/dbname`
   here is the internal db url :postgresql://postgre:ByL8CYXCn7Jelwak2DGEP0ZGdOhW6KjO@dpg-d90ggg5ckfvc73delafg-a/bugtracker_db_c5yf
---

## Step 3: Deploy Django App on Render

1. On Render, click **"New"** → **"Web Service"**

2. Connect GitHub:
   - Click **"Connect Account"** (link your GitHub)
   - Select your `bugtracker` repository
   - Click **"Connect"**

3. Fill in deployment settings:
   - **Name:** `bugtracker-app`
   - **Environment:** `Python 3`
   - **Build Command:** 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
     ```
   - **Start Command:**
     ```
     gunicorn bugtracker.wsgi
     ```
   - **Instance Type:** Free (or paid if needed)

4. Click **"Create Web Service"**

---

## Step 4: Add Environment Variables

While the app is deploying, add environment variables:

1. In your Render web service dashboard, go to **"Environment"**

2. Add these environment variables:

   | Key | Value |
   |---|---|
   | `DEBUG` | `False` |
   | `SECRET_KEY` | [Generate new one - see below] |
   | `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
   | `DB_ENGINE` | `django.db.backends.postgresql` |
   | `DB_NAME` | `bugtracker_db` |
   | `DB_USER` | `postgres` |
   | `DB_PASSWORD` | [Copy from database page] |
   | `DB_HOST` | [Copy from database page] |
   | `DB_PORT` | `5432` |

3. Click **"Save"**

### How to Generate New SECRET_KEY:

Go to Python terminal and run:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the output and paste it as `SECRET_KEY` in Render.

---

## Step 5: Create Admin User

Once deployed, you need to create a superuser.

1. In Render dashboard, go to **"Shell"**

2. Run:
   ```bash
   python manage.py createsuperuser
   ```

3. Follow prompts to create admin account

---

## Step 6: Access Your Website

1. Visit: `https://your-app-name.onrender.com`

2. Admin panel: `https://your-app-name.onrender.com/admin`

3. Login with your superuser credentials

---

## Step 7: Test Dynamic Updates

1. Go to admin panel
2. Add a new bug
3. Visit homepage and verify it appears **instantly**
4. Edit/delete bugs and see real-time updates

---

## How It Works

```
GitHub (Your Code)
    ↓
Render (Detects push)
    ↓
Build: pip install + migrations
    ↓
Deploy: Gunicorn starts
    ↓
PostgreSQL Database (Your Data)
    ↓
Your Website (user visits)
    ↓
Dynamic: Shows current database data
```

**Every time you push to GitHub:**
- Render auto-deploys
- Database schema updates
- Website reflects changes instantly

---

## Common Issues & Solutions

### "Connection refused to database"
- Check DB credentials in environment variables
- Verify PostgreSQL instance is running (check Render dashboard)
- Wait 5 minutes for database to fully initialize

### "Database doesn't exist"
```bash
# In Render Shell:
python manage.py migrate
```

### Styles/Images not showing
```bash
# In Render Shell:
python manage.py collectstatic --no-input
```

### Admin page shows 404
- Make sure `urls.py` includes: `path('admin/', admin.site.urls)`
- Check `INSTALLED_APPS` has `django.contrib.admin`

### "Import modules not found"
- Verify all packages in `requirements.txt`
- Check Build Command runs successfully in logs

---

## Updating Your Website

To deploy new code changes:

```bash
git add .
git commit -m "Your changes"
git push
```

Render will automatically:
1. Detect the push
2. Build your app
3. Run migrations
4. Deploy new version
5. Website updates instantly!

---

## Database Management

To view/edit data directly:

### Option 1: Django Admin Panel
Visit: `https://your-app-name.onrender.com/admin`

### Option 2: Render Dashboard
- Go to your PostgreSQL instance
- Use the built-in query editor

### Backup Your Data
- Render automatically backs up PostgreSQL
- Download backups from database settings

---

## Going from FREE to PAID (optional)

FREE tier has limitations (sleeps after 15 min inactivity).

To upgrade:
1. Click instance type
2. Choose "Pro" or higher
3. Will keep same database & URL
4. No downtime!

---

## Next Steps

✅ Database on PostgreSQL (Render)
✅ Website deployed live
✅ Auto-updates from GitHub

Optional:
- [ ] Setup custom domain
- [ ] Enable HTTPS (automatic on Render)
- [ ] Add email notifications for errors
- [ ] Setup automatic backups

Enjoy your live website! 🚀
