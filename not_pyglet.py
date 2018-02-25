from gtts import gTTS
import time, os

def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = 'temp.mp3'
    file.save(filename)

    os.system('temp.mp3')
   
