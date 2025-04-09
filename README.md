# Conversor de Video a texto

## Analisis
1. Inicialmente, la idea es grabar video, luego extraer el audio, y luego convertirlo a texto utilizando la API de deepgram utilizando los Free Tokens.

### Grabación
2. Utilizaremos el formato de video libre y eficiente VP9.

3. Se puede adaptar la grabación a una parte de la pantalla.(Explicado en requermientos.md)

4. Se puede adaptar nuevamente el script para hacer interactiva la grabación de una parte de la pantalla usando el packete de linux `slop`.También usando xwininfo si deseamos que se adapte a el tamaño de una ventana.(Ambos compatibles SOLO con Xorg)

5. Para el audio utilizaremos el formato Opus.