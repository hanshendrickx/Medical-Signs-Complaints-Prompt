@echo off
setlocal EnableExtensions DisableDelayedExpansion

set "REPO_URL=https://github.com/hanshendrickx/Medical-Signs-Complaints-Prompt.git"
set "REPO_NAME=Medical-Signs-Complaints-Prompt"
set "BRANCH=main"

if /I "%%1"=="" goto menu
if /I "%%1"=="help" goto help
if /I "%%1"=="link" goto link
if /I "%%1"=="status" goto status
if /I "%%1"=="push" goto push
if /I "%%1"=="pull" goto pull
if /I "%%1"=="clone" goto clone
echo [ERROR] Unknown command: %%1
goto help

:menu
echo.
echo ==============================
echo   !GITHUB.CMD Helper
echo ==============================
echo [1] Link repo to origin
echo [2] Push codes to GitHub
echo [3] Pull or update codes
echo [4] Git status
echo [5] Full clone to a folder
echo [0] Exit
set /p CH=Select option: 
if "%%CH%%"=="1" goto link
if "%%CH%%"=="2" goto push
if "%%CH%%"=="3" goto pull
if "%%CH%%"=="4" goto status
if "%%CH%%"=="5" goto clone
if "%%CH%%"=="0" exit /b 0
echo [ERROR] Invalid choice.
goto menu

:help
echo Usage:
echo   !GITHUB.CMD link
echo   !GITHUB.CMD status
echo   !GITHUB.CMD push
echo   !GITHUB.CMD pull
echo   !GITHUB.CMD clone
echo.
echo NOTE: BRANCH is set to %%BRANCH%% at top of this file.
exit /b 0

:ensure_git
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo [ERROR] This folder is not a Git repo.
  exit /b 1
)
exit /b 0

:link
call :ensure_git || exit /b 1
git remote get-url origin >nul 2>&1
if errorlevel 1 (
  git remote add origin "%%REPO_URL%%"
) else (
  git remote set-url origin "%%REPO_URL%%"
)
echo [OK] origin =
git remote get-url origin
exit /b %0%

:status
call :ensure_git || exit /b 1
git status -sb
echo.
git remote -v
exit /b 0

:push
call :ensure_git || exit /b 1
call :link >nul
set /p MSG=Commit message: 
if "%%MSG%%"=="" set "MSG=Update %Mon 03/23/2026% %15:40:50.14%"
git add -A
git diff --cached --quiet >nul 2>&1
if errorlevel 1 (
  git commit -m "%%MSG%%"
  if errorlevel 1 exit /b 1
) else (
  echo [INFO] No file changes to commit.
)
git push -u origin "%%BRANCH%%"
if errorlevel 1 exit /b 1
echo [OK] Push complete.
exit /b 0

:pull
call :ensure_git || exit /b 1
call :link >nul
git fetch origin
if errorlevel 1 exit /b 1
git pull --rebase origin "%%BRANCH%%"
if errorlevel 1 exit /b 1
echo [OK] Pull or update complete.
exit /b 0

:clone
set /p TARGET=Parent folder for full clone default current: 
if "%%TARGET%%"=="" set "TARGET=%C:\Users\hansh\MYSCC26%"
set "DEST=%%TARGET%%\%%REPO_NAME%%"
if exist "%%DEST%%\.git" (
  echo [INFO] Repo already exists: %%DEST%%
  echo [HINT] Open in VS Code: code "%%DEST%%"
  exit /b 0
)
git clone "%%REPO_URL%%" "%%DEST%%"
if errorlevel 1 exit /b 1
echo [OK] Clone complete: %%DEST%%
echo [HINT] Open in VS Code: code "%%DEST%%"
exit /b 0
