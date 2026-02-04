@echo off
:: Lanzador del instalador de Video Downloader
:: Este archivo ejecuta el script de PowerShell

echo ================================================
echo    Descargador de Videos - Instalador
echo ================================================
echo.

powershell -ExecutionPolicy Bypass -File "%~dp0Instalar.ps1"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error al ejecutar el instalador
    pause
)
