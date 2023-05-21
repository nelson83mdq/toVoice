from gtts import gTTS
#from io import BytesIO
import os
import playsound

filename = 'hello_es.mp3'
tts = gTTS("Hola esto es un simulacro, repito esto es una prueba de concepto", lang='es')
tts.save(filename)
playsound.playsound(filename)
#
print('mp3_es')