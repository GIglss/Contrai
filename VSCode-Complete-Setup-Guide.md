# VS Code Complete Environment Replication Guide

## 1. Extension Export & Installation

### Current Extensions (with versions)
Run this command to get your current extensions with versions:
```cmd
code --list-extensions --show-versions
```

### Installation Scripts

#### Batch Script (install-vscode-extensions.bat)
```batch
@echo off
echo Installing VS Code Extensions...
code --install-extension bierner.docs-view
code --install-extension charliermarsh.ruff
code --install-extension github.copilot
code --install-extension github.copilot-chat
code --install-extension github.copilot-labs
code --install-extension llvm-vs-code-extensions.lldb-dap
code --install-extension ms-azuretools.vscode-azure-github-copilot
code --install-extension ms-azuretools.vscode-azure-mcp-server
code --install-extension ms-azuretools.vscode-azureresourcegroups
code --install-extension ms-python.debugpy
code --install-extension ms-python.isort
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.vscode-python-envs
code --install-extension ms-toolsai.jupyter
code --install-extension ms-toolsai.jupyter-keymap
code --install-extension ms-toolsai.jupyter-renderers
code --install-extension ms-toolsai.vscode-ai
code --install-extension ms-toolsai.vscode-ai-remote
code --install-extension ms-toolsai.vscode-jupyter-cell-tags
code --install-extension ms-toolsai.vscode-jupyter-slideshow
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension ms-vscode-remote.remote-ssh-edit
code --install-extension ms-vscode.azure-account
code --install-extension ms-vscode.remote-explorer
code --install-extension sonarsource.sonarlint-vscode
code --install-extension swiftlang.swift-vscode
echo All extensions installed successfully!
pause
```

## 2. VS Code Settings Export

### Export Current Settings
To export your VS Code settings, copy these files from your current machine:

#### User Settings Location (Windows)
```
%APPDATA%\Code\User\settings.json
%APPDATA%\Code\User\keybindings.json
%APPDATA%\Code\User\snippets\
```

#### Export Commands
```cmd
:: Create export directory
mkdir "%USERPROFILE%\Desktop\VSCode-Backup"

:: Copy settings
copy "%APPDATA%\Code\User\settings.json" "%USERPROFILE%\Desktop\VSCode-Backup\"
copy "%APPDATA%\Code\User\keybindings.json" "%USERPROFILE%\Desktop\VSCode-Backup\"

:: Copy snippets folder
xcopy "%APPDATA%\Code\User\snippets" "%USERPROFILE%\Desktop\VSCode-Backup\snippets\" /E /I

:: Copy tasks and launch configurations if they exist
if exist "%APPDATA%\Code\User\tasks.json" copy "%APPDATA%\Code\User\tasks.json" "%USERPROFILE%\Desktop\VSCode-Backup\"
if exist "%APPDATA%\Code\User\launch.json" copy "%APPDATA%\Code\User\launch.json" "%USERPROFILE%\Desktop\VSCode-Backup\"
```

## 3. Import Settings on New Machine

### Restore Settings
```cmd
:: Copy settings back (run on new machine)
copy "path\to\backup\settings.json" "%APPDATA%\Code\User\"
copy "path\to\backup\keybindings.json" "%APPDATA%\Code\User\"
xcopy "path\to\backup\snippets\*" "%APPDATA%\Code\User\snippets\" /E /Y
```

## 4. Workspace Settings Export

### Export Workspace Configuration
```cmd
:: Export current workspace settings
code --list-extensions > workspace-extensions.txt
copy ".vscode\settings.json" workspace-settings.json
copy ".vscode\launch.json" workspace-launch.json
copy ".vscode\tasks.json" workspace-tasks.json
```

## 5. Complete Replication Process

### Step-by-Step Setup for New PC

1. **Install VS Code**
   - Download from https://code.visualstudio.com/
   - Install with default settings

2. **Install Extensions**
   - Run the batch script provided above
   - Or manually install from the extension list

3. **Import Settings**
   - Copy settings.json and keybindings.json to %APPDATA%\Code\User\
   - Copy snippets folder

4. **Sign in to Services**
   - GitHub Copilot: Sign in with GitHub account
   - Azure: Sign in with Azure account
   - Remote SSH: Configure SSH keys if needed

5. **Install Required Tools**
   - Python (if using Python extensions)
   - Node.js (if using JavaScript/TypeScript)
   - Git
   - Java JDK (for Android development)
   - Android Studio (for React Native)

## 6. Automation Script for Complete Setup

### setup-vscode-environment.bat
```batch
@echo off
echo Setting up VS Code Environment...

:: Create backup directory
mkdir "%USERPROFILE%\Desktop\VSCode-Backup" 2>nul

:: Export current settings (if running on source machine)
if exist "%APPDATA%\Code\User\settings.json" (
    echo Backing up current settings...
    copy "%APPDATA%\Code\User\settings.json" "%USERPROFILE%\Desktop\VSCode-Backup\"
    copy "%APPDATA%\Code\User\keybindings.json" "%USERPROFILE%\Desktop\VSCode-Backup\"
    xcopy "%APPDATA%\Code\User\snippets" "%USERPROFILE%\Desktop\VSCode-Backup\snippets\" /E /I /Q
)

:: Export extensions list
echo Exporting extensions list...
code --list-extensions > "%USERPROFILE%\Desktop\VSCode-Backup\extensions.txt"
code --list-extensions --show-versions > "%USERPROFILE%\Desktop\VSCode-Backup\extensions-with-versions.txt"

echo Backup completed! Files saved to %USERPROFILE%\Desktop\VSCode-Backup\
echo.
echo To restore on new machine:
echo 1. Install VS Code
echo 2. Run the extension installation script
echo 3. Copy settings files to %%APPDATA%%\Code\User\
echo.
pause
```

## 7. Extension Categories Summary

Your current setup includes:
- **GitHub Copilot**: AI-powered coding assistant
- **Python Development**: Full Python toolchain (pylance, debugpy, isort, ruff)
- **Jupyter Notebooks**: Complete Jupyter support with renderers and tools
- **Azure Tools**: Azure resource management and GitHub Copilot integration
- **Remote Development**: SSH and remote explorer capabilities
- **Swift Development**: Swift language support
- **Code Quality**: SonarLint for code analysis
- **Documentation**: Docs view for better documentation

This represents a comprehensive development environment suitable for:
- Python development and data science
- Web development (React/TypeScript)
- Mobile development (React Native, Swift)
- Cloud development (Azure)
- Remote development workflows