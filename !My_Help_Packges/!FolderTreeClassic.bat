@echo off
setlocal
cd /d c:\Users\hansh\MYSCC26
if not exist "FolderTrees\!FolderTreeClassic" mkdir "FolderTrees\!FolderTreeClassic"
echo Generating classic folder trees for depths 2,3,4,5...

if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_2.txt" --style simple --icons simple --depth 2
  ".venv\Scripts\python.exe" Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_3.txt" --style simple --icons simple --depth 3
  ".venv\Scripts\python.exe" Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_4.txt" --style simple --icons simple --depth 4
  ".venv\Scripts\python.exe" Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_5.txt" --style simple --icons simple --depth 5
) else (
  py -3 Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_2.txt" --style simple --icons simple --depth 2
  py -3 Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_3.txt" --style simple --icons simple --depth 3
  py -3 Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_4.txt" --style simple --icons simple --depth 4
  py -3 Folder_Tree.py . -o "FolderTrees\!FolderTreeClassic\tree_level_5.txt" --style simple --icons simple --depth 5
)

echo Done. Files are in FolderTrees\!FolderTreeClassic
endlocal
