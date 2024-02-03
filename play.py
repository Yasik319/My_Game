import pygame
from Hero import Hero
import events
from sounds import *
from score import *
from treat import *


def run():
    pygame.init()
    pygame.display.set_caption('SUETA')
    screen = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()
    back = pygame.transform.scale(pygame.image.load(
        'images/1678777727_bogatyr-club-p-pikselnii-lesnoi-fon-foni-pinterest-34.png').convert_alpha(), (1200, 800))
    hero = Hero(screen)
    bots = pygame.sprite.Group()
    eda = pygame.sprite.Group()
    group = pygame.sprite.Group()
    bg_mus()
    scores = Scores(screen)
    pygame.time.set_timer(pygame.USEREVENT, 5000)



    while True:
        fake = fak()
        events.event(group, fake)
        if scores.game:
            screen.blit(back, (0, 0))
            hero.update()
            scores.show_hp(hero)
            scores.show_ples()
            events.make(bots, screen)
            events.broke(hero, bots, group)
            events.make_gd(eda, screen)
            scores.finish(hero)
            events.move_fak(screen, group)
            events.eat(hero, eda, scores)
        pygame.display.update()
        clock.tick(60)