# Requrimientos

## Sistema Operativo

Requiere Linux con Xorg(X11), no es compatible con Wayland 

## Paquetes de Linux

1. `ffmpeg` para grabar
2. `libvpx` para el codec libre VP9

## Pantalla de grabación
1. Utiliza la pantalla predeterminada :0
2. (verificar con `echo $DISPLAY`)
3. Se puede cambiar `pantalla_numero` en el archivo grabar.py

## Grabar una solo una de la pantalla porción

### Configuración de la región a grabar

Se pueden agregar las variables:
```
posicion_x = 100  # Distancia desde el borde izquierdo
posicion_y = 200  # Distancia desde el borde superior
ancho = 800       # Ancho de la región
alto = 600        # Alto de la región
```

Cambiar en comando:  `"-i", "0:"` por: 
```
"-i", f":0.0+{posicion_x},{posicion_y}"
```

Y finalmente cambiar `"-video_size", resolucion,` por:
```
"-video_size", f"{ancho}x{alto}",```
