import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from squirrel import Squirrel


def run_game():
    pygame.init()

    pygame.display.set_caption("Squirrel the Game")
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    squirrel = Squirrel(screen)
    bullets = Group()

    while True:
        gf.check_event(game_settings, screen, squirrel, bullets)
        squirrel.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, squirrel, bullets)


run_game()
