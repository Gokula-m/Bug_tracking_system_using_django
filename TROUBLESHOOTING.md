# Deployment Troubleshooting Guide

## Before You Start

Checklist:
- [ ] Code pushed to GitHub
- [ ] `.env` file NOT in GitHub (check with `git status`)
- [ ] `db.sqlite3` NOT in GitHub
- [ ] `Procfile` exists
- [ ] `runtime.txt` exists
- [ ] `requirements.txt` complete
- [ ] Environment variables set on Render

---

## Issues During Deployment

### Issue 1: "ModuleNotFoundError: No module named 'xxx'"

**Cause:** Package not in `requirements.txt`

**Solution:**
```bash
# Locally, find what's missing:
pip list

# Add to requirements.txt:
pip freeze > requirements.txt

# Push to GitHub:
git add requirements.txt
git commit -m "Update dependencies"
git push
```

---

### Issue 2: "ImportError: No module named 'decouple'"

**Cause:** `python-decouple` not installed on server

**Fix in requirements.txt:**
```
Django==6.0.5
python-decouple==3.8
psycopg2-binary==2.9.9
gunicorn==21.2.0
whitenoise==6.6.0
```

---

### Issue 3: "connection refused to database"

**Cause:** Database credentials wrong or database not ready

**Solutions:**

1. **Check environment variables:**
   - Go to Render dashboard → Web Service → Environment
   - Verify all DB variables match your PostgreSQL instance
   - Copy exact values from database page

2. **Verify database is running:**
   - Go to Render dashboard → PostgreSQL instance
   - Status should be "Available"
   - Wait 5 minutes if just created

3. **Test connection locally:**
   ```bash
   # Update .env with production credentials
   DEBUG=False
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=bugtracker_db
   DB_USER=postgres
   DB_PASSWORD=xxxxx
   DB_HOST=your-host.render.com
   DB_PORT=5432
   
   # Test:
   python manage.py shell
   from django.db import connection
   connection.ensure_connection()  # If no error, connection works
   ```

---

### Issue 4: "Static files not loading (404)"

**Cause:** Didn't run `collectstatic`

**Solution:**

In Build Command, ensure you have:
```bash
python manage.py collectstatic --no-input
```

If already deployed:
1. Go to Render Shell
2. Run: `python manage.py collectstatic --no-input`
3. Redeploy

---

### Issue 5: "No such table: bugs_bug"

**Cause:** Migrations not run

**Solution:**

In Render Shell:
```bash
python manage.py migrate
python manage.py migrate bugs
```

Or redeploy with updated Build Command:
```bash
python manage.py migrate && gunicorn bugtracker.wsgi
```

---

### Issue 6: "Admin page shows 404"

**Cause:** Missing admin URLs

**Check urls.py:**
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # Must have this!
    # ... other urls
]
```

---

### Issue 7: "CSRF verification failed"

**Cause:** Missing or wrong ALLOWED_HOSTS

**Solution:**

Add to Render environment variables:
```
ALLOWED_HOSTS=your-app-name.onrender.com,www.your-app-name.onrender.com
```

---

### Issue 8: "Internal Server Error (500)"

**How to debug:**

1. Go to Render dashboard → Web Service → Logs
2. Look for error messages
3. Common causes:
   - Database connection
   - Missing settings
   - Migration not run
   - Import errors

4. Common fixes:
   ```bash
   # In Render Shell:
   python manage.py migrate
   python manage.py collectstatic --no-input
   ```

---

### Issue 9: "Module 'whitenoise' has no attribute 'middleware'"

**Cause:** Wrong WhiteNoise version

**Fix in requirements.txt:**
```
whitenoise==6.6.0
```

---

### Issue 10: "Render build failed during pip install"

**Cause:** Python version mismatch or system dependency missing

**Solution:**

Ensure `runtime.txt` has:
```
3.11.9
```

And `requirements.txt` has all dependencies:
```
Django==6.0.5
python-decouple==3.8
psycopg2-binary==2.9.9
gunicorn==21.2.0
whitenoise==6.6.0
```

---

## Debugging Techniques

### 1. Check Deployment Logs

Render logs show build & runtime errors:
- Go to "Logs" tab in dashboard
- Read from bottom (newest first)

### 2. Access Shell

Run commands on deployed server:
```bash
cd bugtracker
python manage.py shell
```

### 3. Database Connection Test

```bash
python manage.py dbshell
# If connects, database is accessible
```

### 4. Check Installed Packages

```bash
pip list | grep -i django
```

### 5. Verify Settings

```bash
python manage.py shell
from django.conf import settings
print(settings.DATABASES)
print(settings.ALLOWED_HOSTS)
```

---

## Testing Locally First

**Before pushing to Render, test locally:**

1. Create local `.env`:
   ```
   DEBUG=True
   SECRET_KEY=django-insecure-test
   DB_ENGINE=django.db.backends.sqlite3
   DB_NAME=db.sqlite3
   ```

2. Test migrations:
   ```bash
   python manage.py migrate
   ```

3. Test admin:
   ```bash
   python manage.py createsuperuser
   python manage.py runserver
   # Visit localhost:8000/admin
   ```

4. Add a bug and verify it shows on homepage

If works locally → Should work on Render!

---

## Performance Issues

### Website Loads Slowly

**Potential causes:**
- Database queries too slow
- Missing database indexes
- Large queries without pagination
- Free-tier Render (sleeps after inactivity)

**Solutions:**
1. Upgrade to paid Render tier
2. Add `select_related()` in Django queries
3. Add database indexes
4. Implement caching

---

## Database Issues

### Can't see data in admin

```bash
# In Render Shell:
python manage.py shell
from bugs.models import Bug
Bug.objects.all()  # Should show bugs
```

### Database locked

```bash
# Usually auto-fixes, but try:
python manage.py migrate --no-input
```

---

## Getting Help

1. **Check Build Logs** - Usually shows exact error
2. **Test Locally** - Reproduce issue locally first
3. **Render Support** - https://render.com/support
4. **Django Docs** - https://docs.djangoproject.com/
5. **Stack Overflow** - Tag: django + render

---

## Key Remember Points

✅ **DO:**
- Use environment variables for secrets
- Test locally first
- Check logs when things fail
- Keep `requirements.txt` updated
- Run migrations

❌ **DON'T:**
- Commit `.env` file
- Commit `db.sqlite3`
- Use SQLite in production
- Ignore migration warnings
- Hardcode secrets in settings.py

---

## Quick Redeploy Checklist

When things break:

1. [ ] Check Render logs
2. [ ] Test locally with same `.env`
3. [ ] Run `python manage.py migrate`
4. [ ] Run `python manage.py collectstatic --no-input`
5. [ ] Check database connection
6. [ ] Verify environment variables
7. [ ] Check ALLOWED_HOSTS
8. [ ] Redeploy

Usually one of these fixes it! 🎯
