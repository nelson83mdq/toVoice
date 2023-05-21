import pyttsx3
engine = pyttsx3.init()
# configuracion
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)
voices = engine.getProperty('voices')
for personality in voices:
    print(type(personality))
engine.setProperty('voices', voices[1].id)

for voice in voices:
   if "ES-MX" in voice.id:
      engine.setProperty('voice', voice.id)

engine.say("Esto es una prueba de comunicacion, repito una prueba de comunicacion")
engine.runAndWait()