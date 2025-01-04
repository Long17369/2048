import pygame
from snd import *

# Initialize the game
pygame.init()
pygame.display.set_caption(CONST.WINDOWS_TITLE)
screen = pygame.display.set_mode(CONST.WINDOWS_SIZE)
clock = pygame.time.Clock()

# Game loop
game = Game(is_print=True)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            game.keydown(event)
        if event.type == pygame.KEYUP:
            game.keyup(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse_down(event)
        if event.type == pygame.MOUSEBUTTONUP:
            game.mouse_up(event)
    if game.run == False:
        game = Game(is_print=True)
    game.update()
    pygame.display.flip()
    clock.tick(60)

