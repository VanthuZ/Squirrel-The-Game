import pygame
from pygame.sprite import Group
from service import game_functions as gf
from settings.game_stats import GameStats
from settings.settings import Settings
from game_objects.squirrel import Squirrel


def run_game():
    pygame.init()
    pygame.display.set_caption("Squirrel the Game")

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    squirrel = Squirrel(screen)
    cats = Group()
    bullets = Group()
    stats = GameStats(game_settings)
    gf.create_fleet(game_settings, screen, squirrel, cats)

    while True:
        gf.check_event(game_settings, screen, squirrel, bullets)

        if stats.game_active:
            squirrel.update()
            gf.update_bullets(game_settings, screen, squirrel, cats, bullets)
            gf.update_cats(game_settings, stats, screen, squirrel, cats, bullets)

        gf.update_screen(game_settings, screen, squirrel, cats, bullets)


run_game()
