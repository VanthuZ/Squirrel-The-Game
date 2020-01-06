class Settings:

    def __init__(self):
        """general"""
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (50, 90, 0)
        """bullets"""
        self.bullet_speed_factor = 1
        self.bullets_allowed = 3
        """enemies-cats"""
        self.cat_speed_factor = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        """hero-squirrel"""
        self.lives_limit = 3