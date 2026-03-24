Set-Location 'c:\Users\hansh\MYSCC26'; $content = @'
@echo off
setlocal

set "OUTDIR=FolderTrees"
if not exist "%OUTDIR%" mkdir "%OUTDIR%"

REM Current directory -> FolderTrees/structure.txt
uv run python Folder_Tree.py . -o "%OUTDIR%\structure.txt" --style artisanal --icons artisanal

REM Any folder -> FolderTrees/custom_structure.txt
uv run python Folder_Tree.py C:\path\to\folder -o "%OUTDIR%\custom_structure.txt" --style artisanal --icons artisanal

REM Limited output -> FolderTrees/clean_structure.txt
uv run python Folder_Tree.py . -o "%OUTDIR%\clean_structure.txt" --style artisanal --icons artisanal --max-files 5
'@; Set-Content -Path '!Folder_Tree.bat' -Value $content -Encoding ascii