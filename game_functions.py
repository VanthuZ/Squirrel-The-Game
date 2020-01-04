import sys
import pygame

from Bullet import Bullet


def check_event(game_settings, screen, squirrel, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, squirrel, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, squirrel)


def check_keydown_events(event, game_settings, screen, squirrel, bullets):
    if event.key == pygame.K_RIGHT:
        squirrel.moving_right = True
    elif event.key == pygame.K_LEFT:
        squirrel.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(game_settings, screen, squirrel, bullets)


def check_keyup_events(event, squirrel):
    if event.key == pygame.K_RIGHT:
        squirrel.moving_right = False
    elif event.key == pygame.K_LEFT:
        squirrel.moving_left = False


def fire_bullets(game_settings, screen, squirrel, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, squirrel)
        bullets.add(new_bullet)


def update_screen(game_settings, screen, squirrel, bullets):
    screen.fill(game_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.blitme()

    squirrel.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

