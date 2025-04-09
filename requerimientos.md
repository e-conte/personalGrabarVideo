# Requerimientos

## Sistema Operativo

Requiere Linux con Xorg(X11), no es compatible con Wayland 

## Paquetes de Linux

1. `ffmpeg` - CLI de grabación
2. `libvpx` - Libreria del codec libre VP9 de video
3. `pipewire`+o  `pulseaudio` - Servidores de Audio

## Video - Pantalla de grabación
1. Utiliza la pantalla predeterminada `:0` (Se puede cambiar)
2. Verificar con:
```
echo $DISPLAY
```
3. Si el resultado es ":1" podes cambiar la variable `pantalla_numero` dentro del archivo grabar.py

## Video - Grabar una porción de la pantalla porción
Si deseas grabar solo una porción de la pantalla debes modificar el archivo `grabar.py` de la siguiente manera:

### Configuración de la región a grabar

Agregá las variables:
```
posicion_x = 100  # Distancia desde el borde izquierdo del monitor
posicion_y = 200  # Distancia desde el borde superior del monitor
ancho = 800       # Ancho de la región en pixeles
alto = 600        # Alto de la región en pixeles
```

Cambiá el comando:  `"-i", "0:"` por: 
```
"-i", f":0.0+{posicion_x},{posicion_y}"
```

Y finalmente cambiá `"-video_size", resolucion,` por:
```
"-video_size", f"{ancho}x{alto}",
```

## Audio - Codec
1. Utiliza el codec Opus que suele estar presente en Linux
2. Podes verificar que este instalado con:
```
ldconfig -p | grep libnous
``` 

## Audio - Compatibilidad
1. Es compatible con Pulseaudio y Pipewire.
2. Utiliza Pipewire en modo compatibilidad.
3. Podes verificar si PulseAudio o PipeWire esta presente con: 
```
pactl info | "server name"
```
4. Si no estan presente instala uno de los paquetes `pulseaudio`o `pipewire`