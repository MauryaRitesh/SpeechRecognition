import speech_recognition as sr

from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
except Exception as e:
    print (e)
