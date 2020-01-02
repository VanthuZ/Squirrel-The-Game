import sys
import pygame


def check_event(squirrel):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                squirrel.moving_right = True
            elif event.key == pygame.K_LEFT:
                squirrel.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                squirrel.moving_right = False
            elif event.key == pygame.K_LEFT:
                squirrel.moving_left = False


def update_screen(game_settings, screen, squirrel):

    screen.fill(game_settings.bg_color)
    squirrel.blitme()

    pygame.display.flip()
