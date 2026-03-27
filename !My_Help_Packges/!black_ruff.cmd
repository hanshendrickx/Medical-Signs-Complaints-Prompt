@echo off
setlocal

cd /d C:\Users\hansh\MYSCC26

call .venv\Scripts\activate.bat
if errorlevel 1 exit /b 1

black .
if errorlevel 1 exit /b 1
echo [OK] Finished black

ruff check . --fix
if errorlevel 1 exit /b 1
ruff check .
echo [OK] Finished ruff check

uv run python manage.py check
if errorlevel 1 exit /b 1
echo [OK] Finished ruff check

uv run C:\Users\hansh\MYSCC26\manage.py check
echo [OK] manage.py check.
echo [OK] Finished.
exit /b 0