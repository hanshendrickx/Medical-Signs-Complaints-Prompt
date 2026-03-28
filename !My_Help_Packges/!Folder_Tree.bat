@echo off
setlocal
cd /d c:\Users\hansh\MYSCC26
if not exist "FolderTrees" mkdir "FolderTrees"

if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" Folder_Tree.py . -o "FolderTrees\structure.txt" --style simple --icons simple --depth 3
  rem ".venv\Scripts\python.exe" Folder_Tree.py "C:\path\to\folder" -o "FolderTrees\custom_structure.txt" --style simple --icons simple --depth 3
  ".venv\Scripts\python.exe" Folder_Tree.py . -o "FolderTrees\clean_structure.txt" --style simple --icons simple --depth 3 --max-files 5
) else (
  py -3 Folder_Tree.py . -o "FolderTrees\structure.txt" --style simple --icons simple --depth 3
  rem py -3 Folder_Tree.py "C:\path\to\folder" -o "FolderTrees\custom_structure.txt" --style simple --icons simple --depth 3
  py -3 Folder_Tree.py . -o "FolderTrees\clean_structure.txt" --style simple --icons simple --depth 3 --max-files 5
)
endlocal
