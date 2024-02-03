import pygame
from random import randint

class passive(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.alc = ['alc.png', 'alc_bl(1).png', 'alc331.png']
        self.image = pygame.transform.scale(pygame.image.load('images/'+self.alc[randint(0, 2)]).convert_alpha(), (40, 40))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = randint(1, 1100)
        self.rect.y = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 720:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class goods(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/eda(2).png'), (50, 50))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = randint(1, 1100)
        self.rect.y = 0

    def update(self):
        self.rect.y += 2
        if self.rect.y > 720:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

