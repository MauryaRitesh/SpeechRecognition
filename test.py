import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
text = r.recognize_google(audio)
print (text)

print(' '.join(format(ord(x), 'b') for x in text))
