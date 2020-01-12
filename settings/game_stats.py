import pygame.font


class GameStats():

    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = False

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 100)
        self.level_number = 1
        self.prep_level()


    def reset_stats(self):
        self.lives_left = self.game_settings.lives_limit

    def prep_level(self):
        self.level = self.font.render(str(self.level_number), True, self.text_color, self.game_settings.bg_color)
        self.level_rect = self.level.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.screen_rect.top

    def show_level(self):
        self.screen.blit(self.level, self.level_rect)







