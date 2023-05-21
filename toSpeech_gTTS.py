from gtts import gTTS
from io import BytesIO

#mp3_fp = BytesIO()
tts = gTTS("Hola esto es un simulacro, repito esto es una prueba de concepto", lang='es')
tts.save('hello_es.mp3')
#tts.write_to_fp(mp3_fp)
print('mp3_es')