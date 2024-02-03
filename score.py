import pygame
from Hero import *

class Scores():
    def __init__(self, screen):
        self.img_hp = pygame.transform.scale(pygame.image.load('images/zigh(1).png').convert_alpha(), (50, 50))
        self.hrum = pygame.transform.scale(pygame.image.load('images/vkusno(1).png').convert_alpha(), (50, 50))
        self.screen = screen
        self.cnt = 0
        self.game = True

    def show_hp(self, hero):
        x = 10
        for hp in range(hero.health):
            self.screen.blit(self.img_hp, (x, 20))
            x += 50

    def show_ples(self):
        print_cnt = pygame.font.SysFont('Roman', 50).render(str(self.cnt), True, (209, 52, 52))
        self.screen.blit(self.hrum, (1050, 20))
        self.screen.blit(print_cnt, (1110, 10))

    def finish(self, hero):
        if hero.health < 1:
            finish_t = pygame.font.SysFont('TunnelFront', 100).render('Абонент больше не абонент', True, (209, 52, 52))
            self.screen.blit(finish_t, (200, 400))
            self.game = False
        elif self.cnt > 9:
            finish_t = pygame.font.SysFont('TunnelFront', 300).render('Чё ты за ЛЕВ!', True, (209, 52, 52))
            self.screen.blit(finish_t, (200, 400))
            self.game = False