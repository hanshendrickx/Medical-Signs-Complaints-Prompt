@echo off
REM run this script by [CTRL+F5]
setlocal

cd /d %~dp0

set "PY=.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Missing %PY%
  echo Run: uv sync
  exit /b 1
)

echo [1/3] Django check...
"%PY%" manage.py check
if errorlevel 1 exit /b 1

echo [2/3] Applying migrations...
"%PY%" manage.py migrate
if errorlevel 1 exit /b 1

echo [3/3] Starting server at http://127.0.0.1:8000/
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000/"
"%PY%" manage.py runserver 127.0.0.1:8000
