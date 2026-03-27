@echo off 
setlocal 
cd /d %~dp0 
 
set "PY_EXE=.venv\Scripts\python.exe" 
if not exist "%PY_EXE%" ( 
  echo [ERROR] Missing venv python: %PY_EXE% 
  echo Create the environment first, then re-run this script. 
  exit /b 1
) 
 
echo [1/2] Running Django system check... 
"%PY_EXE%" manage.py check 
if errorlevel 1 exit /b 1
 
set "SMOKE=import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','scc.settings'); import django; django.setup(); from django.template.loader import get_template; [get_template(n) for n in ('account/login.html','account/signup.html','account/logout.html','account/password_set.html')]; print('OK: templates load')" 
echo [2/2] Running auth template smoke test... 
"%PY_EXE%" -c "%SMOKE%" 
if errorlevel 1 exit /b 1
 
echo [PASS] All checks succeeded.
exit /b 0
