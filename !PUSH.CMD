@echo off
cd /d c:\Users\hansh\MYSCC26
git init
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/hanshendrickx/Medical-Signs-Complaints-Prompt.git
git add -A .
git commit -m "Push from MYSCC26"
git push -u origin main

setlocal EnableExtensions DisableDelayedExpansion

REM Always run from this script's folder
pushd "%~dp0"

set "REPO_URL=https://github.com/hanshendrickx/Medical-Signs-Complaints-Prompt.git"
set "BRANCH=main"

echo [INFO] Checking git repo...
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo [ERROR] Not a git repo in this folder.
  echo [HINT] Run: git init
  pause
  popd
  exit /b 1
)

for /f "delims=" %%I in ('git rev-parse --show-toplevel 2^>nul') do set "TOP=%%~fI"
for %%I in ("%CD%") do set "CUR=%%~fI"

if /I not "%TOP%"=="%CUR%" (
  echo [ERROR] Active git root is:
  echo        %TOP%
  echo [ERROR] Current folder is:
  echo        %CUR%
  echo [HINT] You are inside a parent repo. Fix that first, then retry.
  pause
  popd
  exit /b 1
)

echo [INFO] Setting origin...
git remote get-url origin >nul 2>&1
if errorlevel 1 (
  git remote add origin "%REPO_URL%"
) else (
  git remote set-url origin "%REPO_URL%"
)

set /p MSG=Commit message (Enter for auto):
if "%MSG%"=="" set "MSG=Update %DATE% %TIME%"

git add -A .
git diff --cached --quiet >nul 2>&1
if errorlevel 1 (
  git commit -m "%MSG%"
  if errorlevel 1 (
    echo [ERROR] Commit failed.
    pause
    popd
    exit /b 1
  )
) else (
  echo [INFO] Nothing new to commit.
)

git push -u origin "%BRANCH%"
if errorlevel 1 (
  echo [ERROR] Push failed.
  pause
  popd
  exit /b 1
)

echo [OK] Push complete to %REPO_URL%
pause
popd
exit /b 0