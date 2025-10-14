# VS Code Extensions Export

## Current Extensions List
bierner.docs-view
charliermarsh.ruff
github.copilot
github.copilot-chat
github.copilot-labs
llvm-vs-code-extensions.lldb-dap
ms-azuretools.vscode-azure-github-copilot
ms-azuretools.vscode-azure-mcp-server
ms-azuretools.vscode-azureresourcegroups
ms-python.debugpy
ms-python.isort
ms-python.python
ms-python.vscode-pylance
ms-python.vscode-python-envs
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-ai
ms-toolsai.vscode-ai-remote
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode-remote.remote-ssh
ms-vscode-remote.remote-ssh-edit
ms-vscode.azure-account
ms-vscode.remote-explorer
sonarsource.sonarlint-vscode
swiftlang.swift-vscode

## Installation Commands

### Windows (PowerShell)
```powershell
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
```

### Batch Installation Script
Save this as `install-extensions.bat`:
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
echo Done!
pause
```

### PowerShell Script (install-extensions.ps1)
```powershell
$extensions = @(
    "bierner.docs-view",
    "charliermarsh.ruff",
    "github.copilot",
    "github.copilot-chat",
    "github.copilot-labs",
    "llvm-vs-code-extensions.lldb-dap",
    "ms-azuretools.vscode-azure-github-copilot",
    "ms-azuretools.vscode-azure-mcp-server",
    "ms-azuretools.vscode-azureresourcegroups",
    "ms-python.debugpy",
    "ms-python.isort",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.vscode-python-envs",
    "ms-toolsai.jupyter",
    "ms-toolsai.jupyter-keymap",
    "ms-toolsai.jupyter-renderers",
    "ms-toolsai.vscode-ai",
    "ms-toolsai.vscode-ai-remote",
    "ms-toolsai.vscode-jupyter-cell-tags",
    "ms-toolsai.vscode-jupyter-slideshow",
    "ms-vscode-remote.remote-ssh",
    "ms-vscode-remote.remote-ssh-edit",
    "ms-vscode.azure-account",
    "ms-vscode.remote-explorer",
    "sonarsource.sonarlint-vscode",
    "swiftlang.swift-vscode"
)

Write-Host "Installing VS Code Extensions..." -ForegroundColor Green
foreach ($extension in $extensions) {
    Write-Host "Installing $extension..." -ForegroundColor Yellow
    code --install-extension $extension
}
Write-Host "All extensions installed!" -ForegroundColor Green
```