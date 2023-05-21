"""
    Author: Brizuela, Nelson Damian
    fecha:  13.4.2023
    el codigo permite transformar un texto pasado por argumento, a una voz en español latino.
"""


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