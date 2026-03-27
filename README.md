## Quick Setup
# Restart via !restart_scc.cmd
1.  ✅ **Base_Tools**: Windows 10, VSCode, Django6, Python 3.14, .Dotenv, Black, Russ
2.  ✅ **Extra Packages**: REST, django debug_Toolbar, Allauth, corsheaders, CSRF
3.  ✅ **Font** Noto Sans Google font, International USeng+Dutch
4.  ✅ **!restart_scc.cmd with tests** R-click file and "run" via [CTRL+F5]
5.  ✅ **!sync_black_ruff_env.bat** R-click file and "run" via [CTRL+F5]
6.  ✅ **Folder_Tree** To create pro folder trees

6.  Run the setup batch file:

7.  ✅ **Secure authentication** for family members and Anonymous Guest
8.  ✅ **safe production-aware** safe cleanup settings
9.  ✅ **Private data storage** with encryption
10. ✅ **REST API** for symptom and complaint collection
11. ✅ **AI prompt generation** for medical analysis
12. ✅ **Family member profiles** for all ages
13. ✅ **Proxy for Children and Disabled member profiles** for all ages, depening         .on international law and customs
14. ✅ **Doctor preparation tools**

## CMD Recovery

Run this from project root when migrations or DB history get stuck:

```bat
recover_django.cmd
```

The script backs up `db.sqlite3` to `db.sqlite3.pre_recovery.bak`, rebuilds migrations, runs migrate, and runs check.

# README.md SCC Signs and Current Complaints App
# SCC App - Signs and Current Complaints

A secure, private medical data collection app for families to track symptoms and prepare for doctor appointments.

## Features



- 🔐 **Maximum Security** - End-to-end encryption, strong password policies, JWT tokens
- 👨‍👩‍👧‍👦 **Family Accounts** - Manage health data for all family members
- 📝 **Symptom Tracking** - Log signs and current complaints
- 🤖 **AI-Ready Summaries** - Generate structured prompts for medical AI analysis
- 🏥 **Doctor Preparation** - Get answers to: "Do I need a doctor?", patient guidelines, physician guidelines, and follow-up questions

📂 MYSCC26/
├─ 📁 accounts/
│ ├─ 📁 __pycache__/
│ │ ├─ 📄 __init__.cpython-314.pyc
│ │ ├─ 📄 admin.cpython-314.pyc
│ │ ├─ 📄 apps.cpython-314.pyc
│ │ ├─ 📄 models.cpython-314.pyc
│ │ ├─ 📄 urls.cpython-314.pyc
│ │ └─ ... (1 more files)
│ ├─ 📂 migrations/
│ │ ├─ 📁 __pycache__/
│ │ ├─ 🐍 0001_initial.py
│ │ └─ 🐍 __init__.py
│ ├─ 🐍 __init__.py
│ ├─ 🐍 admin.py
│ ├─ 🐍 apps.py
│ ├─ 🐍 models.py
│ ├─ 🐍 tests.py
│ └─ ... (2 more files)
├─ 📁 complaints/
│ ├─ 📁 __pycache__/
│ │ ├─ 📄 __init__.cpython-314.pyc
│ │ ├─ 📄 admin.cpython-314.pyc
│ │ ├─ 📄 apps.cpython-314.pyc
│ │ └─ 📄 models.cpython-314.pyc
│ ├─ 📂 migrations/
│ │ ├─ 📁 __pycache__/
│ │ ├─ 🐍 0001_initial.py
│ │ └─ 🐍 __init__.py
│ ├─ 🐍 __init__.py
│ ├─ 🐍 admin.py
│ ├─ 🐍 ai_summary.py
│ ├─ 🐍 apps.py
│ ├─ 🐍 models.py
│ └─ ... (3 more files)
├─ 📂 docs/
│ ├─ 📝 api.md
│ ├─ 📝 security.md
│ ├─ 📄 security.pdf
│ └─ 📝 setup.md
├─ 📁 Folder_Trees/
│ ├─ 📄 clean_structure.txt
│ └─ 📄 structure.txt
├─ 📁 FolderTrees/
│ └─ 📄 structure.txt
├─ 📁 media/
├─ 📁 scc/
│ ├─ 📁 __pycache__/
│ │ ├─ 📄 __init__.cpython-314.pyc
│ │ ├─ 📄 settings.cpython-314.pyc
│ │ ├─ 📄 urls.cpython-314.pyc
│ │ └─ 📄 wsgi.cpython-314.pyc
│ ├─ 🐍 __init__.py
│ ├─ 🐍 asgi.py
│ ├─ 📝 DISCLAIMER FOR MEDICAL APP.md
│ ├─ 📄 DISCLAIMER FOR MEDICAL APP.pdf
│ ├─ 📄 LICENSE
│ └─ ... (5 more files)
├─ 📂 static/
│ ├─ 📁 css/
│ ├─ 📁 images/
│ └─ 📁 js/
├─ 📂 templates/
│ ├─ 📁 accounts/
│ │ ├─ 📁 accounts/
│ │ ├─ 🌐 base.html
│ │ └─ 🌐 home.html
│ └─ 🌐 base.html
├─ ⚙️ !Folder_Tree.bat
├─ 📄 !restart_scc.cmd
├─ ⚙️ !restartVE.bat
├─ ⚙️ !sync_black_ruff_env.bat
├─ 🐍 _patch_home.py
└─ ... (17 more files)

--------------------------------------------------------------------------------
Total Folders: 22
Total Files: 47
Total Size: 116.9 KB

# Create a simple home view
## powershell!!!!!!!!!!!!!!!!!!!
$homeView = @"
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# FamilyMembers + Guest
Added to settings.py

## Errors
InconsistentMigrationHistory — the old db.sqlite3 has allauth's account migrations applied before your new accounts migrations existed. Fix: delete the DB and remigrate fresh.

\`\`\`

The app follows best practices for medical data security while remaining simple and fast to use. You can extend it by adding more symptom categories, integrating with actual AI APIs, or adding export features for sharing with doctors.

You're absolutely right! Python 3.14 was released in October 2025 and Django 6.0 followed in December 2025 with native support for Python 3.14 . Using uv for this is a perfect choice—it's 10-100x faster than pip and provides modern dependency management .

Here's a complete setup script using uv for your SCC (Signs and Current Complaints) app:

# Powershell:
#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Sets up the SCC (Signs and Current Complaints) Django app using uv
.DESCRIPTION
    Initializes a new Django 6.0 project with Python 3.14, sets up apps for
    accounts and complaints, and installs all required dependencies
.NOTES
    Author: SCC App Setup
    Requires: uv (https://astral.sh/uv)
#>

Write-Host "🚀 Setting up SCC (Signs and Current Complaints) App with uv" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Green

# Check if uv is installed
try {
    $uvVersion = uv --version
    Write-Host "✅ uv is installed: $uvVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ uv is not installed. Installing now..." -ForegroundColor Yellow
    Write-Host "Installing uv for Windows..." -ForegroundColor Cyan
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

    # Refresh environment
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Create project directory
Write-Host "`n📁 Creating project directory..." -ForegroundColor Cyan
$projectName = "scc_app"
if (Test-Path $projectName) {
    Write-Host "⚠️ Directory $projectName already exists. Removing..." -ForegroundColor Yellow
    Remove-Item -Path $projectName -Recurse -Force
}

# Initialize project with uv
Write-Host "`n📦 Initializing project with uv..." -ForegroundColor Cyan
uv init $projectName
Set-Location $projectName

# Remove the default hello.py
Remove-Item hello.py -Force

# Add dependencies
Write-Host "`n📥 Installing core dependencies..." -ForegroundColor Cyan
uv add "django>=6.0.0"
uv add "djangorestframework>=3.15.0"
uv add "django-cors-headers>=4.3.0"
uv add "django-allauth>=0.60.0"
uv add "djangorestframework-simplejwt>=5.3.0"
uv add "pillow>=10.2.0"  # For image handling
uv add "python-dotenv>=1.0.0"
uv add "psycopg2-binary>=2.9.0"  # PostgreSQL support

# Add development dependencies
Write-Host "`n📥 Installing development dependencies..." -ForegroundColor Cyan
uv add --dev "ruff>=0.4.0"  # Fast linting
uv add --dev "pre-commit>=3.5.0"
uv add --dev "pytest>=8.0.0"
uv add --dev "pytest-django>=4.8.0"
uv add --dev "model-bakery>=1.17.0"  # Test fixtures
uv add --dev "coverage>=7.4.0"

# Create Django project
Write-Host "`n🏗️ Creating Django project..." -ForegroundColor Cyan
uv run django-admin startproject config .
uv run python manage.py startapp accounts
uv run python manage.py startapp complaints

# Create additional directories
Write-Host "`n📁 Creating project structure..." -ForegroundColor Cyan
New-Item -ItemType Directory -Path "templates" -Force | Out-Null
New-Item -ItemType Directory -Path "templates/accounts" -Force | Out-Null
New-Item -ItemType Directory -Path "templates/complaints" -Force | Out-Null
New-Item -ItemType Directory -Path "static/css" -Force | Out-Null
New-Item -ItemType Directory -Path "static/js" -Force | Out-Null
New-Item -ItemType Directory -Path "media" -Force | Out-Null
New-Item -ItemType Directory -Path "docs" -Force | Out-Null

# Features

- 🔐 **Maximum Security** - Django 6.0 CSP, strong password policies, JWT tokens
- 👨‍👩‍👧‍👦 **Family Accounts** - Manage health data for all family members
- 📝 **Symptom Tracking** - Log signs and current complaints
- 🤖 **AI-Ready Summaries** - Generate structured prompts for medical AI analysis
- 🏥 **Doctor Preparation** - Get answers to 4 key questions

## Tech Stack

- Python 3.14
- Django 6.0
- Django REST Framework
- uv for package management

# Important codes
REM restart via C:\Users\"username"\scc_app\!restart.bat
cd /d C:\Users\hansh\scc_app
call "!restart.bat"

# Create initial files
Write-Host "`n📝 Creating initial files..." -ForegroundColor Cyan

# Create .gitignore
@"
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so
.Python
*.egg
*.egg-info/
dist/
build/
.venv/
venv/
env/

# Django
*.log
local_settings.py
media/
staticfiles/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Coverage
.coverage
htmlcov/

# Project specific
*.db
*.sqlite3
.env
.python-version
"@ | Out-File -FilePath ".gitignore" -Encoding utf8

# Create .python-version to lock Python version
@"
3.14
"@ | Out-File -FilePath ".python-version" -Encoding utf8

# Create pyproject.toml configuration for ruff
$pyprojectPath = "pyproject.toml"
$pyprojectContent = Get-Content $pyprojectPath -Raw

# Add ruff configuration to pyproject.toml
$ruffConfig = @"

[tool.ruff]
line-length = 88
target-version = "py314"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "C4"]
ignore = []

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.pytest.ini_options]
DJANGO_SETTINGS_MODULE = "config.settings"
python_files = ["tests.py", "test_*.py", "*_tests.py"]
"@

$pyprojectContent + $ruffConfig | Out-File -FilePath $pyprojectPath -Encoding utf8

# Create pre-commit config
@"
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format
"@ | Out-File -FilePath ".pre-commit-config.yaml" -Encoding utf8

# Create a basic README
@"
# SCC App - Signs and Current Complaints

A secure, private medical data collection app for families to track symptoms and prepare for doctor appointments.

## Features

- 🔐 **Maximum Security** - Django 6.0 CSP, strong password policies, JWT tokens
- 👨‍👩‍👧‍👦 **Family Accounts** - Manage health data for all family members
- 📝 **Symptom Tracking** - Log signs and current complaints
- 🤖 **AI-Ready Summaries** - Generate structured prompts for medical AI analysis
- 🏥 **Doctor Preparation** - Get answers to 4 key questions

## Tech Stack

- Python 3.14
- Django 6.0
- Django REST Framework
- uv for package management

## Quick Start

1. **Install uv** (if not already):
   \`\`\`powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   \`\`\`

2. **Run the setup script**:
   \`\`\`powershell
   .\setup_scc_app.ps1
   \`\`\`

3. **Activate the virtual environment**:
   \`\`\`powershell
   .venv\Scripts\activate
   \`\`\`

4. **Run migrations**:
   \`\`\`powershell
   uv run python manage.py migrate
   \`\`\`

5. **Create a superuser**:
   \`\`\`powershell
   uv run python manage.py createsuperuser
   \`\`\`

6. **Run the development server**:
   \`\`\`powershell
   uv run python manage.py runserver
   \`\`\`

## Project Structure

\`\`\`
scc_app/
├── config/               # Django project settings
├── accounts/             # Family accounts app
├── complaints/           # Signs and complaints app
├── templates/            # HTML templates
├── static/               # Static files
├── media/                # User uploaded files
├── docs/                 # Documentation
├── .venv/                # Virtual environment
├── pyproject.toml        # Project configuration
├── uv.lock               # Locked dependencies
└── manage.py             # Django management script
\`\`\`

## License

MIT
"@ | Out-File -FilePath "README.md" -Encoding utf8

# Create a simple home view
$homeView = @"
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', {'user': request.user})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
"@
New-Item -ItemType File -Path "complaints/views.py" -Force -Value $homeView

# Create a basic home template
$homeTemplate = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SCC App - Signs and Current Complaints</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif; line-height: 1.6; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }
        .feature { padding: 20px; background: #f8f9fa; border-radius: 5px; }
        .btn { display: inline-block; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        .btn:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏥 SCC App</h1>
        <p>Signs and Current Complaints - Your personal medical assistant</p>

        <div class="features">
            <div class="feature">
                <h3>🔐 Secure & Private</h3>
                <p>Family-only access with maximum security</p>
            </div>
            <div class="feature">
                <h3>📋 Track Symptoms</h3>
                <p>Log signs and current complaints easily</p>
            </div>
            <div class="feature">
                <h3>🤖 AI-Ready</h3>
                <p>Generate structured summaries for medical AI</p>
            </div>
            <div class="feature">
                <h3>🏥 Doctor Prep</h3>
                <p>Know when to see a doctor and what to ask</p>
            </div>
        </div>

        {% if user.is_authenticated %}
            <a href="/dashboard/" class="btn">Go to Dashboard</a>
            <a href="/admin/logout/" class="btn" style="background: #dc3545;">Logout</a>
        {% else %}
            <a href="/admin/login/" class="btn">Login</a>
        {% endif %}
    </div>
</body>
</html>
"@
New-Item -ItemType File -Path "templates/home.html" -Force -Value $homeTemplate

# Update config/settings.py
$settingsPath = "config/settings.py"
$settingsContent = Get-Content $settingsPath -Raw

# Add installed apps and other configurations
$newSettings = $settingsContent -replace "INSTALLED_APPS = \[", @"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third party
    'rest_framework',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework_simplejwt',

    # Local
    'accounts',
    'complaints',
"@

# Add template directories
$newSettings = $newSettings -replace "TEMPLATES = \[", @"
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
"@

# Add CSP settings for Django 6.0
$cspSettings = @"

# Django 6.0 Content Security Policy
from django.utils.csp import CSP

SECURE_CSP = {
    "default-src": [CSP.SELF],
    "script-src": [CSP.SELF, CSP.NONCE],
    "style-src": [CSP.SELF, "https://fonts.googleapis.com"],
    "font-src": [CSP.SELF, "https://fonts.gstatic.com"],
    "img-src": [CSP.SELF, "data:"],
}

# Security Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/hour',
        'user': '100/hour',
    }
}

# JWT Settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
}
"@

$newSettings = $newSettings + "`n" + $cspSettings
$newSettings | Out-File -FilePath $settingsPath -Encoding utf8

# Update config/urls.py
$urlsPath = "config/urls.py"
$urlsContent = @"
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from complaints.views import home, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/complaints/', include('complaints.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"@
$urlsContent | Out-File -FilePath $urlsPath -Encoding utf8

# Install pre-commit hooks
Write-Host "`n🔧 Installing pre-commit hooks..." -ForegroundColor Cyan
uv run pre-commit install

# Run initial migrations
Write-Host "`n🔄 Running initial migrations..." -ForegroundColor Cyan
uv run python manage.py migrate

Write-Host "`n✨ Setup complete!" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Green
Write-Host "`n📋 Next steps:" -ForegroundColor Yellow
Write-Host "1. Activate the virtual environment: .venv\Scripts\activate"
Write-Host "2. Create a superuser: uv run python manage.py createsuperuser"
Write-Host "3. Start the server: uv run python manage.py runserver"
Write-Host "4. Visit http://127.0.0.1:8000/ in your browser"
Write-Host "`n📚 Project structure:" -ForegroundColor Cyan
Write-Host "- config/          : Django project settings"
Write-Host "- accounts/        : Family accounts app (you'll build this)"
Write-Host "- complaints/      : Signs and complaints app (you'll build this)"
Write-Host "- templates/       : HTML templates"
Write-Host "- pyproject.toml   : Project dependencies"
Write-Host "- uv.lock          : Locked dependencies"

Write-Host "`n🚀 Happy coding!" -ForegroundColor Green.gith

# Renew Migrations AND remove old migrations
REM 1. Delete the stale database
del db.sqlite3CCCC

REM 2. Delete all migration files (keep __init__.py)
del /q accounts\migrations\0*.py
del /q complaints\migrations\0*.py

REM 3. Recreate fresh migrations
uv run python manage.py makemigrations accounts
uv run python manage.py makemigrations complaints

REM 4. Apply them
uv run python manage.py migrate

# Temporary Guest Access (48 hours)
You want users to be able to use the app without creating a permanent account, with access expiring after 48 hours. There are a few ways to do this. I'll outline two simple approaches – you can choose what fits your vision.
## Option A: Session‑Based Guest Data (No User Account)
Use Django’s session framework to store the user's complaints, symptoms, etc., tied to their session cookie.

Set session expiry to 48 hours (SESSION_COOKIE_AGE = 48 * 3600 in settings).

No need to create a User object. The guest can just start using the app.

Later, if they decide to register, you could copy the session data to their new user account.

Pros: Simple, no extra database tables.
Cons: Data is lost if the user clears cookies or switches browsers. No way to log in on another device.


## Option B: Temporary User Account with Expiry
Extend your FamilyUser model with a is_temporary boolean and expires_at datetime.

When a guest starts, automatically create a user with a random username (e.g., guest_<uuid>), mark it temporary, set expiry to 48 hours from now.

After expiry, you can have a cron job or a middleware that blocks login and deletes old temporary users.