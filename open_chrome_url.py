import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
try:
    text = r.recognize_google(audio)
    print('You said:\n' + text)
    wb.get(chrome_path).open(text)
 
except Exception as e:
    print (e)
