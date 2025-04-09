# Requrimientos

## Sistema Operativo

Requiere Linux con Xorg(X11), no es compatible con Wayland 

## Paquetes de Linux

1. `ffmpeg` para grabar
2. `libvpx` para el codec libre VP9

## Pantalla de grabación
1. Utiliza la pantalla predeterminada `:0`
2. Verificar con `echo $DISPLAY`
3. Se puede cambiar en `pantalla_numero` dentro del archivo grabar.py

## Grabar una porción de la pantalla porción
Si deseas grabar solo una porción de la pantalla debes modificar el archivo `grabar.py` de la siguiente manera:

### Configuración de la región a grabar

Agregá las variables:
```
posicion_x = 100  # Distancia desde el borde izquierdo
posicion_y = 200  # Distancia desde el borde superior
ancho = 800       # Ancho de la región
alto = 600        # Alto de la región
```

Cambiá el comando:  `"-i", "0:"` por: 
```
"-i", f":0.0+{posicion_x},{posicion_y}"
```

Y finalmente cambiá `"-video_size", resolucion,` por:
```
"-video_size", f"{ancho}x{alto}",
```
