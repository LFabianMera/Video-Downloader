# Script para crear el paquete de distribucion completo

Write-Host "Creando paquete de distribucion..." -ForegroundColor Cyan

$distFolder = "dist"
$packageName = "Video-Downloader-Package"
$packagePath = Join-Path $PSScriptRoot $packageName

# Crear carpeta del paquete si no existe
if (Test-Path $packagePath) {
    Remove-Item $packagePath -Recurse -Force
}
New-Item -ItemType Directory -Path $packagePath | Out-Null

# Copiar archivos necesarios
Write-Host "Copiando archivos..." -ForegroundColor Yellow
Copy-Item (Join-Path $distFolder "Video-Downloader.exe") $packagePath
Copy-Item (Join-Path $distFolder "Instalar.bat") $packagePath
Copy-Item (Join-Path $distFolder "Instalar.ps1") $packagePath
Copy-Item (Join-Path $distFolder "LEEME.txt") $packagePath

# Crear archivo ZIP
Write-Host "Creando archivo ZIP..." -ForegroundColor Yellow
$zipPath = "$packageName.zip"
if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}
Compress-Archive -Path $packagePath -DestinationPath $zipPath

Write-Host ""
Write-Host "[OK] Paquete creado exitosamente!" -ForegroundColor Green
Write-Host "Archivo: $zipPath" -ForegroundColor Green
Write-Host ""
Write-Host "Contenido del paquete:" -ForegroundColor Cyan
Write-Host "  - Video-Downloader.exe    (Aplicacion principal)" -ForegroundColor White
Write-Host "  - Instalar.bat            (Instalador automatico)" -ForegroundColor White
Write-Host "  - Instalar.ps1            (Script de instalacion)" -ForegroundColor White
Write-Host "  - LEEME.txt               (Instrucciones)" -ForegroundColor White
Write-Host ""
Write-Host "Listo para distribuir!" -ForegroundColor Green
