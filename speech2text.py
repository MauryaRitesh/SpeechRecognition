import speech_recognition as sr
import webbrowser as wb
import speak

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
    lang = 'en'

    speak.tts(text, lang)

    f_text = 'https://www.google.co.in/search?q=' + text
    wb.get(chrome_path).open(f_text)
 
except Exception as e:
    print (e)
