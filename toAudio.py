from gtts import gTTS
import sys
import os
import playsound

toAudio = sys.argv[1]
print(type(toAudio))
filename = 'hhhh.mp3'
tts = gTTS(text=toAudio, lang='es')
tts.save(filename)
#playsound.playsound(filename)
#os.remove(filename)
#
print(toAudio)