@echo off
setlocal

cd /d %~dp0

set "PY=.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Missing venv python: %PY%
  echo Create the environment first, then re-run this script.
  exit /b 1
)

echo [1/6] Verifying Django import...
"%PY%" -c "import django; print('Django ' + django.get_version())"
if errorlevel 1 goto :fail

if exist "db.sqlite3" (
  echo [2/6] Backing up db.sqlite3 to db.sqlite3.pre_recovery.bak...
  copy /Y "db.sqlite3" "db.sqlite3.pre_recovery.bak" >nul
  if errorlevel 1 goto :fail

  echo [3/6] Resetting database file...
  del /Q "db.sqlite3"
  if errorlevel 1 goto :fail
) else (
  echo [2/6] No db.sqlite3 found. Skipping backup/reset.
)

echo [4/6] Generating migrations for local apps...
"%PY%" manage.py makemigrations accounts complaints
if errorlevel 1 goto :fail

echo [5/6] Applying migrations...
"%PY%" manage.py migrate
if errorlevel 1 goto :fail

echo [6/6] Running Django system check...
"%PY%" manage.py check
if errorlevel 1 goto :fail

echo [OK] Recovery completed successfully.
echo You can now run: "%PY%" manage.py runserver
exit /b 0

:fail
echo [FAILED] Recovery stopped due to an error.
if exist "db.sqlite3.pre_recovery.bak" echo Backup is available at db.sqlite3.pre_recovery.bak
exit /b 1
