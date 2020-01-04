import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game_settings, screen, squirrel):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/nut2.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = squirrel.rect.centerx
        self.rect.top = squirrel.rect.top

        self.y = float(self.rect.y)
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)