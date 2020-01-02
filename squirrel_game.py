import pygame

import game_functions as gf
from settings import Settings
from squirrel import Squirrel


def run_game():
    pygame.init()

    pygame.display.set_caption("Squirrel the Game")
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    squirrel = Squirrel(screen)

    while True:

        gf.check_event()
        gf.update_screen(game_settings, screen, squirrel)


run_game()
