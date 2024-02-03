import pygame
from play import *


pygame.init()
width, height = 1050, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Peter the Piglet")
from Hero import *




screen.fill((0, 0, 0))
font = pygame.font.Font(None, 75)
text = font.render("Hello, Bro! Let's see how strong you are!", True, (100, 255, 100))
text_x = 10
text_y = 100
screen.blit(text, (text_x, text_y))

button_font = pygame.font.SysFont(None, 80)
button_text_color = pygame.Color("green")
button_color = pygame.Color("black")
button_rect = pygame.Rect(width // 4, 140, 150, 100)
button_text = button_font.render('Start drink!', True, button_text_color)
pygame.draw.rect(screen, button_color, button_rect)
button_rect_center = button_text.get_rect(center=button_rect.center)
screen.blit(button_text, button_rect_center)


hero = Hero(screen)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                run()
