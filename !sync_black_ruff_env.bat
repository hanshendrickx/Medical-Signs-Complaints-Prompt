@echo off
setlocal

REM Run from this script directory
cd /d "%~dp0"
if errorlevel 1 exit /b 1

REM Optional reset commands:
REM taskkill /f /im python.exe
REM del db.sqlite3
REM uv run python manage.py makemigrations complaints
REM uv run python manage.py migrate
REM uv run python manage.py createsuperuser

where uv >nul 2>&1
if errorlevel 1 (
    echo [ERROR] uv is not installed or not in PATH.
    exit /b 1
)

REM Use project-local Ruff cache to avoid user-profile cache conflicts
set "RUFF_CACHE_DIR=.ruff_cache"
if not exist "%RUFF_CACHE_DIR%" md "%RUFF_CACHE_DIR%"

uv sync --dev
if errorlevel 1 exit /b 1

REM Pick ONE formatter strategy:
REM Strategy A: Ruff formatter + Ruff lint
uv run ruff format .
if errorlevel 1 exit /b 1

uv run ruff check --fix .
if errorlevel 1 exit /b 1

uv run ruff format --check .
if errorlevel 1 exit /b 1

uv run ruff check .
if errorlevel 1 exit /b 1

REM If you prefer Black instead, remove Ruff format lines and keep:
REM uv run black .
REM if errorlevel 1 exit /b 1

uv run python manage.py check
if errorlevel 1 exit /b 1

echo [OK] Environment sync and checks completed successfully.
exit /b 0