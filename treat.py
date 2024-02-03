import pygame
from random import randint


class fak(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/fad(1).png'), (75, 75))
        self.rect = self.image.get_rect(center=(randint(1,1000), 0))


    def update(self):
        self.rect.y += 1
        if self.rect.y > 720:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)