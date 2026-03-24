@echo off
REM run this script by [CTRL+F5]
setlocal
cmd
cd MYSCC26
.venv\Scripts\activate.bat
echo [3/3] Starting server at http://127.0.0.1:8000/
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000/"
"%PY%" manage.py runserver 127.0.0.1:8000
