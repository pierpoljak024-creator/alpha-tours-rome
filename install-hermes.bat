@echo off
echo ============================================
echo   HERMES AGENT — Alpha Tours Rome Setup
echo ============================================
echo.
echo Hermes v0.12.0 will be installed from GitHub.
echo You'll need: OpenRouter API key + (optional) Modal token
echo.

:: Step 1 — Install Hermes from GitHub
echo [1/5] Installing Hermes Agent from GitHub...
pip install git+https://github.com/NousResearch/hermes-agent.git 2>&1
if %ERRORLEVEL% neq 0 (
    echo ! Failed to install Hermes. Check Python/pip setup.
    pause
    exit /b 1
)
echo Done.
echo.

:: Step 2 — Verify installation
echo [2/5] Verifying installation...
hermes --version 2>&1
if %ERRORLEVEL% neq 0 (
    echo ! Trying python -m hermes...
    python -m hermes --version 2>&1
    if %ERRORLEVEL% neq 0 (
        echo ! Hermes not found. Trying pip show...
        pip show hermes-agent 2>&1 | findstr Version
        echo.
        echo Hermes is installed! Just use "hermes" directly (not python -m)
        echo.
    )
)
echo Done.
echo.

:: Step 3 — Run setup wizard
echo [3/5] Launching Hermes setup wizard...
echo This will guide you through selecting your provider (OpenRouter recommended)
echo and entering your API key.
echo.
echo NOTE: When prompted, select "openrouter" as your inference provider.
echo Your OpenRouter API key looks like: sk-or-v1-xxxxxxxxxxxx
echo.
echo Get your key at: https://openrouter.ai/keys
echo.
echo Press any key to start the wizard...
pause >nul
hermes setup
echo Done.
echo.

:: Step 4 — Optionally configure Modal backend
echo [4/5] Modal serverless backend (optional)
echo Hermes also supports Modal for cloud functions.
echo Get Modal tokens at: https://modal.com/settings/tokens
echo.
echo To set up Modal later, run:
echo   hermes config set terminal.backend modal
echo   modal token set --token-id YOUR_ID --token-secret YOUR_SECRET
echo.
timeout /t 3 >nul

:: Step 5 — Gateway setup (optional)
echo [5/5] Messaging gateway setup (optional)
echo Enable Telegram or WhatsApp bot for 24/7 automated customer support.
echo.
echo For Telegram:
echo   1. Open Telegram, search for @BotFather
echo   2. Send /newbot, choose a name (e.g. "Alpha Tours Rome Bot")
echo   3. Copy the API token BotFather gives you
echo   4. Run: hermes gateway add telegram
echo   5. Paste your token when prompted
echo.
echo For WhatsApp:
echo   Use the Business API — run: hermes whatsapp
echo.

echo ============================================
echo   HERMES INSTALLED SUCCESSFULLY!
echo ============================================
echo.
echo Quick start:
echo   hermes                    Start interactive chat
echo   hermes model              Change model/provider
echo   hermes -z "Your question"  One-shot query (script-friendly)
echo   hermes gateway            Start messaging gateway
echo   hermes gateway install    Auto-start on boot
echo   hermes doctor             Check config and deps
echo.
echo IMPORTANT: Hermes auto-loads AGENTS.md from the current directory.
echo Our AGENTS.md is ready at: %CD%\AGENTS.md
echo.  
echo IMPORTANT: When specifying a model, use the plain model name without  
echo the provider prefix. Example:  
echo   CORRECT:  google/gemini-2.0-flash-001  
echo   WRONG:    openrouter/google/gemini-2.0-flash-001  
echo.  
echo Try running: hermes -z "What tours do you offer?" --provider openrouter  
echo.  
pause
