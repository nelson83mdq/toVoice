import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    #print("Sphinx thinks you said " + r.recognize_google(audio, language="es_ES"))
    text = r.recognize_google(audio, language="es-ES")
    if 'comando 1' in text.lower():
        print('1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ')
    if 'comando 2' in text.lower():
        print('2 2 2 2 2 2 2 2 2 2 2 2 2 ')
    print(text)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

