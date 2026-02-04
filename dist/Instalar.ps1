# Descargador de Videos - Instalador
# Este script instala FFmpeg automáticamente si no está disponible

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   Descargador de Videos - Instalador" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si FFmpeg está instalado
Write-Host "Verificando FFmpeg..." -ForegroundColor Yellow
$ffmpegInstalled = $false

try {
    $ffmpegVersion = ffmpeg -version 2>$null
    if ($LASTEXITCODE -eq 0) {
        $ffmpegInstalled = $true
        Write-Host "[OK] FFmpeg ya esta instalado" -ForegroundColor Green
    }
} catch {
    $ffmpegInstalled = $false
}

# Instalar FFmpeg si no está disponible
if (-not $ffmpegInstalled) {
    Write-Host "[!] FFmpeg no esta instalado" -ForegroundColor Red
    Write-Host ""
    Write-Host "FFmpeg es necesario para que la aplicacion funcione correctamente." -ForegroundColor Yellow
    Write-Host "Permite descargar videos en diferentes formatos y calidades." -ForegroundColor Yellow
    Write-Host ""
    
    $response = Read-Host "Deseas instalar FFmpeg automaticamente? (S/N)"
    
    if ($response -eq "S" -or $response -eq "s") {
        Write-Host ""
        Write-Host "Instalando FFmpeg..." -ForegroundColor Yellow
        Write-Host "Esto puede tardar unos minutos..." -ForegroundColor Yellow
        Write-Host ""
        
        try {
            winget install --id=Gyan.FFmpeg -e --silent
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "[OK] FFmpeg instalado exitosamente" -ForegroundColor Green
                Write-Host ""
                Write-Host "[IMPORTANTE] Debes reiniciar esta ventana para que FFmpeg funcione" -ForegroundColor Yellow
                Write-Host "Cierra esta ventana y ejecuta el instalador nuevamente." -ForegroundColor Yellow
                Write-Host ""
                Read-Host "Presiona Enter para cerrar"
                exit
            } else {
                Write-Host "[ERROR] No se pudo instalar FFmpeg automaticamente" -ForegroundColor Red
                Write-Host "Instalalo manualmente desde: https://ffmpeg.org/download.html" -ForegroundColor Yellow
                Write-Host ""
                Read-Host "Presiona Enter para salir"
                exit 1
            }
        } catch {
            Write-Host "[ERROR] Error al instalar FFmpeg: $_" -ForegroundColor Red
            Write-Host "Instalalo manualmente desde: https://ffmpeg.org/download.html" -ForegroundColor Yellow
            Write-Host ""
            Read-Host "Presiona Enter para salir"
            exit 1
        }
    } else {
        Write-Host ""
        Write-Host "Instalacion cancelada." -ForegroundColor Yellow
        Write-Host "La aplicacion no funcionara sin FFmpeg." -ForegroundColor Red
        Write-Host "Puedes instalarlo manualmente desde: https://ffmpeg.org/download.html" -ForegroundColor Yellow
        Write-Host ""
        Read-Host "Presiona Enter para salir"
        exit 1
    }
}

# Ejecutar la aplicación
Write-Host ""
Write-Host "Iniciando aplicacion..." -ForegroundColor Green
Write-Host ""

$exePath = Join-Path $PSScriptRoot "Video-Downloader.exe"

if (Test-Path $exePath) {
    Start-Process $exePath
    Write-Host "[OK] Aplicacion iniciada" -ForegroundColor Green
    Write-Host ""
    Write-Host "Puedes cerrar esta ventana." -ForegroundColor Gray
} else {
    Write-Host "[ERROR] No se encontro Video-Downloader.exe" -ForegroundColor Red
    Write-Host "Asegurate de que este archivo este en la misma carpeta que el instalador." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Presiona Enter para salir"
    exit 1
}
