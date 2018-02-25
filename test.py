from gtts import gTTS
import pygame
import time, os

def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = 'temp.mp3'
    file.save(filename)

    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print "Playing..."
        clock.tick(1000)
