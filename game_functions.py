import sys
import pygame


def check_event():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(game_settings, screen, squirrel):

    screen.fill(game_settings.bg_color)
    squirrel.blitme()

    pygame.display.flip()
