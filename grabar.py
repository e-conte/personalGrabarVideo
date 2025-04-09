from datetime import datetime
import subprocess

global archivo_grabacion, duracion_grabacion

#   Definimos el archivo de salida en formato YY-MM-DD-HH-MM.webm
fecha_y_hora = datetime.now()
archivo_grabacion = fecha_y_hora.strftime("%d-%m-%Y-%Hhs%Mm") + ".webm"

resolucion = "1920x1080"
fps = 30
crf = 30 # calidad
pantalla_numero = ":0"

comando = [
    "ffmpeg",
    "-f", "x11grab",    # Especifica Xorg
    "-video_size", resolucion,
    "-framerate", str(fps),
    "-i","0:" ,   # Pantalla Ppal (verificar con `echo $DISPLAY`)
    "-c:v", "libvpx-vp9",   # Codec Libre VP9 buena relación compresión calidad
    "-crf", str(crf),   # Calidad
    "-b:v", pantalla_numero,    # Se desabilita para que mande "crf"
    "-f", "pulse",  # Captura de audio (Linux/PulseAudio)
    "-i", "default",  # Dispositivo de audio predeterminado
    "-c:a", "libopus", "-b:a", "128k",  # Codec Opus buena relación compresión calidad
    archivo_grabacion
]

try:
    subprocess.run(comando, check=True)
except subprocess.CalledProcessError as e:
    print("Error al grabar" + str(e.returncode))