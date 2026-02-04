# Video Downloader 🎥

Aplicación de escritorio para descargar videos y audio de múltiples plataformas.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

## 🎯 Características

- ✅ Interfaz gráfica intuitiva con Tkinter
- ✅ Descarga de videos en múltiples calidades (Mejor, 720p, 480p)
- ✅ Extracción de audio en formato MP3
- ✅ Soporte para múltiples plataformas
- ✅ Barra de progreso y log de estado en tiempo real
- ✅ Selección personalizada de carpeta de destino
- ✅ Ejecutable standalone (.exe) incluido

## 🌐 Plataformas Soportadas

- YouTube
- TikTok
- Facebook
- Instagram
- Twitter/X
- Y muchas más...

## 📦 Instalación

### Para Usuarios (Ejecutable)

1. Descargar el archivo `Video-Downloader-Package.zip` desde [Releases](../../releases)
2. Descomprimir el archivo
3. Ejecutar `Instalar.bat`
4. El instalador verificará e instalará FFmpeg automáticamente si es necesario
5. ¡Listo para usar!

### Para Desarrolladores

1. Clonar el repositorio:
```bash
git clone https://github.com/LFabianMera/Video-Downloader.git
cd Video-Downloader
```

2. Crear entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Instalar FFmpeg:
```bash
winget install --id=Gyan.FFmpeg -e
```

5. Ejecutar la aplicación:
```bash
python app.py
```

## 🚀 Uso

1. Copia la URL del video que deseas descargar
2. Pega la URL en el campo correspondiente
3. Selecciona el formato:
   - **Video (MP4)**: Descarga el video completo
   - **Audio (MP3)**: Solo descarga el audio
4. Elige la calidad deseada
5. Selecciona la carpeta de destino
6. Haz clic en **DESCARGAR**
7. Observa el progreso en el log

## 🛠️ Tecnologías

- **Python 3.13**
- **yt-dlp**: Descarga de videos
- **Tkinter**: Interfaz gráfica
- **FFmpeg**: Procesamiento de video/audio
- **PyInstaller**: Creación de ejecutable

## 📋 Requisitos

- Windows 10/11
- FFmpeg (se instala automáticamente con el instalador)
- Python 3.9+ (solo para desarrolladores)

## 🔧 Compilar el Ejecutable

Para crear el archivo .exe:

```bash
pyinstaller --onefile --windowed --name "Video-Downloader" app.py
```

O usar el script incluido:
```bash
.\Crear-Paquete.ps1
```

## 🐛 Solución de Problemas

### Error: "FFmpeg no está instalado"
**Solución**: Ejecutar `Instalar.bat` o instalar FFmpeg manualmente:
```bash
winget install --id=Gyan.FFmpeg -e
```

### El ejecutable no abre
**Solución**: 
1. Verificar que Windows Defender no esté bloqueando el archivo
2. Clic derecho > Propiedades > Desbloquear
3. Ejecutar como administrador

### Warning: "JavaScript runtime"
**Solución**: Es solo una advertencia, no afecta la descarga

## 📝 Notas Legales

Esta herramienta debe usarse únicamente para descargar contenido del cual tienes derechos o permiso para descargar. 

Respeta los términos de servicio de cada plataforma y las leyes de derechos de autor.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Leiner Fabián Mera**

- GitHub: [@LFabianMera](https://github.com/LFabianMera)
- Portfolio: [LFabianMera.github.io](https://lfabianmera.github.io)

## ⭐ Agradecimientos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Motor de descarga
- [FFmpeg](https://ffmpeg.org/) - Procesamiento multimedia

---

⭐ Si te gusta este proyecto, dale una estrella en GitHub!
