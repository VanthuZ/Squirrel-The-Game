import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1020))
    pygame.display.set_caption("Squirrel the Game")
    bg_color = (50, 90, 0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()


run_game()