@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 main.py
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo No se encontro Python. Instala Python 3 y activa Add python.exe to PATH.
    ) else (
        python main.py
    )
)
pause
