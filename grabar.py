from datetime import datetime
import subprocess

global archivo_grabacion, duracion_grabacion

#   Definimos el archivo de salida en formato YY-MM-DD-HH-MM.webm
fecha_y_hora = datetime.now()
archivo_grabacion = fecha_y_hora.strftime("%d-%m-%Y-%Hhs%Mm") + ".webm"

