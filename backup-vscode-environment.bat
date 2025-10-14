@echo off
echo VS Code Environment Backup Tool
echo ==============================
echo.

:: Create backup directory
set BACKUP_DIR=%USERPROFILE%\Desktop\VSCode-Environment-Backup
echo Creating backup directory: %BACKUP_DIR%
mkdir "%BACKUP_DIR%" 2>nul

:: Export extensions list
echo Exporting extensions list...
code --list-extensions > "%BACKUP_DIR%\extensions.txt"
code --list-extensions --show-versions > "%BACKUP_DIR%\extensions-with-versions.txt"

:: Backup settings if they exist
if exist "%APPDATA%\Code\User\settings.json" (
    echo Backing up VS Code settings...
    copy "%APPDATA%\Code\User\settings.json" "%BACKUP_DIR%\" >nul
    echo - settings.json backed up
) else (
    echo - No settings.json found
)

if exist "%APPDATA%\Code\User\keybindings.json" (
    copy "%APPDATA%\Code\User\keybindings.json" "%BACKUP_DIR%\" >nul
    echo - keybindings.json backed up
) else (
    echo - No keybindings.json found
)

:: Backup snippets folder
if exist "%APPDATA%\Code\User\snippets" (
    echo Backing up snippets...
    xcopy "%APPDATA%\Code\User\snippets" "%BACKUP_DIR%\snippets\" /E /I /Q >nul
    echo - snippets folder backed up
) else (
    echo - No snippets folder found
)

:: Backup workspace settings if in a workspace
if exist ".vscode\settings.json" (
    echo Backing up workspace settings...
    copy ".vscode\settings.json" "%BACKUP_DIR%\workspace-settings.json" >nul
    echo - workspace settings backed up
)

if exist ".vscode\launch.json" (
    copy ".vscode\launch.json" "%BACKUP_DIR%\workspace-launch.json" >nul
    echo - workspace launch config backed up
)

if exist ".vscode\tasks.json" (
    copy ".vscode\tasks.json" "%BACKUP_DIR%\workspace-tasks.json" >nul
    echo - workspace tasks config backed up
)

echo.
echo ==============================
echo Backup completed successfully!
echo ==============================
echo.
echo Files saved to: %BACKUP_DIR%
echo.
echo Contents:
dir "%BACKUP_DIR%" /b
echo.
echo To restore on a new machine:
echo 1. Install VS Code
echo 2. Copy install-vscode-extensions.bat to new machine and run it
echo 3. Copy settings files to %%APPDATA%%\Code\User\ on new machine
echo 4. Restart VS Code
echo.
pause