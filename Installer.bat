@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b 1
)

REM Run the Python script to check and install packages
python check_and_install_packages.py

pause