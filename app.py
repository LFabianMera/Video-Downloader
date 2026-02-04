import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import yt_dlp

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Descargador de Videos/Audio")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Variables
        self.download_path = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
        self.url = tk.StringVar()
        self.format_choice = tk.StringVar(value="video")
        self.quality_choice = tk.StringVar(value="best")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="Descargador de Videos y Audio", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Plataformas soportadas
        platforms_label = ttk.Label(main_frame, 
                                    text="✓ YouTube | ✓ TikTok | ✓ Facebook | ✓ Instagram",
                                    font=("Arial", 9))
        platforms_label.grid(row=1, column=0, columnspan=3, pady=5)
        
        # URL Input
        ttk.Label(main_frame, text="URL del video:", font=("Arial", 10)).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        url_entry = ttk.Entry(main_frame, textvariable=self.url, width=60)
        url_entry.grid(row=3, column=0, columnspan=3, pady=5, padx=5)
        
        # Formato
        format_frame = ttk.LabelFrame(main_frame, text="Formato", padding="10")
        format_frame.grid(row=4, column=0, columnspan=3, pady=10, padx=5, sticky=(tk.W, tk.E))
        
        ttk.Radiobutton(format_frame, text="Video (MP4)", variable=self.format_choice, 
                       value="video").grid(row=0, column=0, padx=10)
        ttk.Radiobutton(format_frame, text="Audio (MP3)", variable=self.format_choice, 
                       value="audio").grid(row=0, column=1, padx=10)
        
        # Calidad
        quality_frame = ttk.LabelFrame(main_frame, text="Calidad", padding="10")
        quality_frame.grid(row=5, column=0, columnspan=3, pady=10, padx=5, sticky=(tk.W, tk.E))
        
        ttk.Radiobutton(quality_frame, text="Mejor calidad", variable=self.quality_choice, 
                       value="best").grid(row=0, column=0, padx=10)
        ttk.Radiobutton(quality_frame, text="720p", variable=self.quality_choice, 
                       value="720p").grid(row=0, column=1, padx=10)
        ttk.Radiobutton(quality_frame, text="480p", variable=self.quality_choice, 
                       value="480p").grid(row=0, column=2, padx=10)
        
        # Carpeta de destino
        dest_frame = ttk.Frame(main_frame)
        dest_frame.grid(row=6, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        
        ttk.Label(dest_frame, text="Guardar en:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(dest_frame, textvariable=self.download_path, width=45).grid(
            row=0, column=1, padx=5)
        ttk.Button(dest_frame, text="Seleccionar", command=self.select_folder).grid(
            row=0, column=2)
        
        # Botón de descarga
        download_btn = ttk.Button(main_frame, text="DESCARGAR", 
                                 command=self.start_download, style="Accent.TButton")
        download_btn.grid(row=7, column=0, columnspan=3, pady=15, ipadx=30, ipady=5)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(main_frame, length=600, mode='indeterminate')
        self.progress.grid(row=8, column=0, columnspan=3, pady=10)
        
        # Log de estado
        ttk.Label(main_frame, text="Estado:", font=("Arial", 10, "bold")).grid(
            row=9, column=0, sticky=tk.W)
        self.log_text = scrolledtext.ScrolledText(main_frame, height=10, width=75, 
                                                  state='disabled', wrap=tk.WORD)
        self.log_text.grid(row=10, column=0, columnspan=3, pady=5)
        
    def select_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
            
    def log(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        
    def start_download(self):
        url = self.url.get().strip()
        if not url:
            messagebox.showerror("Error", "Por favor ingresa una URL válida")
            return
            
        # Ejecutar descarga en un hilo separado
        thread = threading.Thread(target=self.download, daemon=True)
        thread.start()
        
    def download(self):
        url = self.url.get().strip()
        download_path = self.download_path.get()
        format_type = self.format_choice.get()
        quality = self.quality_choice.get()
        
        # Configurar opciones de yt-dlp
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'progress_hooks': [self.progress_hook],
        }
        
        if format_type == "audio":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
            self.log("📻 Descargando audio en formato MP3...")
        else:
            if quality == "best":
                ydl_opts['format'] = 'bestvideo+bestaudio/best'
            elif quality == "720p":
                ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
            elif quality == "480p":
                ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
            self.log(f"🎥 Descargando video en calidad {quality}...")
        
        try:
            self.progress.start()
            self.log(f"🔗 URL: {url}")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                self.log(f"📄 Título: {info.get('title', 'Desconocido')}")
                self.log(f"📁 Guardando en: {download_path}")
                self.log("⏳ Descargando...")
                
                ydl.download([url])
                
            self.progress.stop()
            self.log("✅ ¡Descarga completada exitosamente!")
            messagebox.showinfo("Éxito", "¡Descarga completada!")
            
        except Exception as e:
            self.progress.stop()
            error_msg = f"❌ Error durante la descarga: {str(e)}"
            self.log(error_msg)
            messagebox.showerror("Error", error_msg)
            
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            self.log(f"⬇ Progreso: {percent} | Velocidad: {speed}")
        elif d['status'] == 'finished':
            self.log("✓ Descarga finalizada, procesando archivo...")

def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
