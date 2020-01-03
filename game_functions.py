import sys
import pygame


def check_event(squirrel):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, squirrel)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, squirrel)

                
def check_keydown_events(event, squirrel):
    if event.key == pygame.K_RIGHT:
        squirrel.moving_right = True
    elif event.key == pygame.K_LEFT:
        squirrel.moving_left = True


def check_keyup_events(event, squirrel):
    if event.key == pygame.K_RIGHT:
        squirrel.moving_right = False
    elif event.key == pygame.K_LEFT:
        squirrel.moving_left = False


def update_screen(game_settings, screen, squirrel):

    screen.fill(game_settings.bg_color)
    squirrel.blitme()

    pygame.display.flip()
