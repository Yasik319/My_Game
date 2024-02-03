import pygame


def bg_mus():
    pygame.mixer.music.load('sounds/hon.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.02)

def drink_mus():
    wat = pygame.mixer.Sound('sounds/sound.mp3')
    wat.play()
    wat.set_volume(0.1)

def eat_mus():
    eat = pygame.mixer.Sound('sounds/z_uk-kushaet.mp3')
    eat.play()
    eat.set_volume(0.1)

def hell_mus():
    hell = pygame.mixer.Sound('sounds/hor.mp3')
    hell.play()
    hell.set_volume(0.1)