@echo off
echo VS Code Environment Restore Tool
echo ================================
echo.

set /p BACKUP_PATH="Enter the path to your backup folder: "

if not exist "%BACKUP_PATH%" (
    echo Error: Backup folder not found!
    pause
    exit /b 1
)

echo Restoring VS Code environment from: %BACKUP_PATH%
echo.

:: Restore settings
if exist "%BACKUP_PATH%\settings.json" (
    echo Restoring settings.json...
    copy "%BACKUP_PATH%\settings.json" "%APPDATA%\Code\User\" >nul
    echo - settings.json restored
) else (
    echo - No settings.json found in backup
)

if exist "%BACKUP_PATH%\keybindings.json" (
    echo Restoring keybindings.json...
    copy "%BACKUP_PATH%\keybindings.json" "%APPDATA%\Code\User\" >nul
    echo - keybindings.json restored
) else (
    echo - No keybindings.json found in backup
)

:: Restore snippets
if exist "%BACKUP_PATH%\snippets" (
    echo Restoring snippets...
    xcopy "%BACKUP_PATH%\snippets\*" "%APPDATA%\Code\User\snippets\" /E /Y /Q >nul
    echo - snippets restored
) else (
    echo - No snippets found in backup
)

:: Install extensions
if exist "%BACKUP_PATH%\extensions.txt" (
    echo.
    echo Installing extensions from backup...
    for /f "tokens=*" %%i in (%BACKUP_PATH%\extensions.txt) do (
        echo Installing %%i...
        code --install-extension %%i
    )
    echo - All extensions installed
) else (
    echo - No extensions list found in backup
)

:: Restore workspace settings if present
if exist "%BACKUP_PATH%\workspace-settings.json" (
    echo.
    echo Workspace settings found in backup.
    echo You may want to copy these to your project's .vscode folder:
    echo - workspace-settings.json
    if exist "%BACKUP_PATH%\workspace-launch.json" echo - workspace-launch.json
    if exist "%BACKUP_PATH%\workspace-tasks.json" echo - workspace-tasks.json
)

echo.
echo ================================
echo Restore completed successfully!
echo ================================
echo.
echo Please restart VS Code to ensure all settings and extensions are loaded properly.
echo.
pause