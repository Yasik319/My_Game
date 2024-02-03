import pygame

class Hero:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images/norm.png').convert_alpha(), (150, 100))
        self.rect = self.image.get_rect(center=(600, 650))
        self.speed = 3
        self.health = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < 1200:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        self.screen.blit(self.image, self.rect)