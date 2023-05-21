import pyttsx3
import sys
engine = pyttsx3.init()

voiceKey = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
engine.setProperty('voice', value= voiceKey)

engine.say(text=sys.argv[1])
engine.runAndWait()
