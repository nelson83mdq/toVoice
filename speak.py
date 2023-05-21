"""
    Author: Brizuela, Nelson Damian
    fecha:  13.4.2023
    el codigo permite transformar un texto pasado por argumento, a una voz en español latino.
"""

"""
# texto de voz
#   
import pyttsx3
import sys
engine = pyttsx3.init('sapi5')
voiceKey = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
engine.setProperty('voice', value= voiceKey)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+1)

def Say(speech):
    engine.say(text=speech)
    engine.runAndWait()

Say(sys.argv[1])
"""

#
# reconocimiento de voz
#
"""
#speechRecognition

import speech_recognition as sr
import webbrowser
j = 'chanCjo'
ear = sr.Recognizer()
for attempt in range(3):
    with sr.Microphone() as source:
        print("hola soy su asistente de voz..{}".format(attempt))
        audio = ear.listen(source)
        try:
            text = ear.recognize_google(audio)
            print("estas diciendo: {}".format(text))
            #print(text)
            print(type(text))
        except:
            print("inentendible...")
"""
