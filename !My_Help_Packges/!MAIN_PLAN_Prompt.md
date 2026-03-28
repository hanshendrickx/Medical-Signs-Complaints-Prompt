# SCC MAIN_PLAN_Prompt
Copy and paste this at the start of every new session to give the AI your exact context.
https://github.com/hanshendrickx/Medical-Signs-Complaints-Prompt


markdown
# SCC PROJECT – MAIN PLAN
Django6 Py3.14 REST Bootstrap5 READ THIS PROMPT BEFORE ADVICING NEW CODES!

## Project Identity
**SCC (Signs and Current Complaints)** is a secure medical data collection and triage app for families. It helps users document symptoms, generate AI‑ready medical prompts, and prepare for doctor visits. The ultimate goal is a phone‑first SCC app with a live prompt builder and longitudinal storage.

## Core Architecture (FINAL – DO NOT CHANGE)

### 1. App Names
- **Custom app:** `accounts` (plural) – handles user profiles, family accounts, authentication
- **Second app:** `complaints` – handles signs, complaints, AI summaries
- **Project folder:** `scc/` (contains settings, urls, wsgi)

### 2. Template Structure (ROOT‑BASED)
All templates live in **root `/templates`**, NOT in app folders.
templates/
├── base.html # Project‑wide base template
├── accounts/ # YOUR custom templates
│ ├── home.html # Main landing page (dual‑panel SCC app goes here)
│ ├── about.html
│ ├── profile.html
│ └── base.html (optional app‑specific base)
└── account/ # ALLAUTH templates (DO NOT MOVE)
├── login.html
├── signup.html
├── logout.html
├── email_confirm.html
├── email/
│ ├── email_confirmation_message.txt
│ └── email_confirmation_subject.txt
└── (other allauth templates)

text

**Why:** Root templates are centralized, easier to maintain, and work perfectly with allauth.

### 3. Django Settings (`scc/settings.py`)
- `INSTALLED_APPS` includes: `'accounts'`, `'complaints'`, `'allauth'`, `'allauth.account'`, `'rest_framework'`, etc.
- `TEMPLATES` setting:
  ```python
  TEMPLATES = [{
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [BASE_DIR / 'templates'],   # ← root templates folder
      'APP_DIRS': True,
      ...
  }]
AUTH_USER_MODEL = 'accounts.FamilyUser' (custom user model)

AUTHENTICATION_BACKENDS includes allauth backend and Django’s default

4. URLs Structure
Main scc/urls.py:

python
path('accounts/', include('allauth.urls')),        # allauth web views
path('api/auth/', include('accounts.urls')),       # your JWT API endpoints
path('', include('accounts.urls')),                # your custom views (home, etc.)
accounts/urls.py contains your JWT endpoints (login, signup, me, family, etc.)

5. Authentication
Web: allauth handles session‑based login (/accounts/login/)

API: SimpleJWT for token authentication (/api/auth/login/)

Guest mode: Temporary users with 48‑hour sessionStorage (no database write)

6. Packages Installed
Django 6.0, Python 3.14

django‑allauth (email confirmation, social login)

djangorestframework + simplejwt

django‑cors‑headers

Bootstrap 5 (frontend)

uv for package management

Black + Ruff for formatting/linting

7. Current Development Goal
Build a dual‑panel SCC app integrated into templates/accounts/home.html:

Left panel: Live PROMPT builder (military compact format, real‑time updates)

Right panel: Phone‑style SCC flow with:

Emergency detection (three‑tier urgency: HIGH/MEDIUM/LOW)

Auto‑call countdown for HIGH urgency (user can cancel)

Staccato free‑text complaint input (AI detects type and urgency)

Photo upload with AI interpretation (simulated or real API)

Voice input (Web Speech API)

Minimal SOCRATES (onset, severity, progression only)

Guest mode: 48‑hour demo using sessionStorage

Longitudinal storage: Save completed sessions to database (authenticated users)

8. Constraints & Rules
DO NOT rename the accounts app or move templates to accounts/templates/

DO NOT change allauth’s template folder name (account stays singular)

DO NOT use app‑level templates for your custom pages – root /templates/accounts/ is the correct location

DO NOT modify allauth’s core templates unless overriding via root templates/account/

ALL new SCC app development goes into templates/accounts/home.html and static files

9. Git & Deployment
Repository: https://github.com/hanshendrickx/Medical-Signs-Complaints-Prompt

Main branch is stable

Use !restart_scc.cmd to restart server with tests

Use !sync_black_ruff_env.bat to format/lint

When You Start a New Session
Paste this MAIN_PLAN_Prompt first. Then state your specific task. The AI will have correct context and won’t make false assumptions.