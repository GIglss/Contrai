@echo off
echo Installing VS Code Extensions...
echo.

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

echo.
echo All extensions installed successfully!
echo Please restart VS Code to ensure all extensions are properly loaded.
pause