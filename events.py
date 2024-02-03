from passive import *
from random import randint
import pygame
from sounds import *
from score import *

def make(bots, screen):
    bots.update()
    bots.draw(screen)
    if len(bots) < 5:
        passiv = passive(randint(5, 6))
        bots.add(passiv)

def make_gd(eda, screen):
    eda.update()
    eda.draw(screen)
    if len(eda) < 5:
        hrum = goods(randint(5, 6))
        eda.add(hrum)

def event(group, fak):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            treat(group, fak)
        if event.type == pygame.QUIT:
            exit()

def broke(hero, bots, group):
    if pygame.sprite.spritecollide(hero, bots, True):
        drink_mus()
        hero.health -= 1
    if pygame.sprite.spritecollide(hero, group, True):
        if hero.health < 3:
            hero.health += 1
            hell_mus()

def treat(group, fak):
    group.add(fak)

def move_fak(screen, group):
    group.update()
    group.draw(screen)


def eat(hero, eda, score):
    if pygame.sprite.spritecollide(hero, eda, True):
        eat_mus()
        score.cnt += 1

