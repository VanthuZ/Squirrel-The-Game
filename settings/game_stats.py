class GameStats():

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.lives_left = self.game_settings.lives_limit