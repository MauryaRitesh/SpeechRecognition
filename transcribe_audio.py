import speech_recognition as sr

r = sr.Recognizer()

audio = 'audio.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    print (text)
    
except Exception as e:
    print (e)
