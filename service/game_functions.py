import sys
from time import sleep

import pygame

from game_objects.bullet import Bullet
from game_objects.cat import Cat


def check_event(game_settings, game_stats, play_button, screen, squirrel, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, squirrel, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, squirrel)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_stats, play_button, mouse_x, mouse_y)


def check_play_button(game_stats, play_button, mouse_x, mouse_y):

       if play_button.rect.collidepoint(mouse_x, mouse_y):
            game_stats.game_active = True


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


def update_screen(game_settings, game_stats, screen, squirrel, cats, bullets, play_button):

    screen.fill(game_settings.bg_color)
    squirrel.blitme()
    cats.draw(screen)

    for bullet in bullets.sprites():
        bullet.blitme()

    if not game_stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(game_settings, screen, squirrel, cats, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_cat_collisions(game_settings, screen, squirrel, cats, bullets)


def check_bullet_cat_collisions(game_settings, screen, squirrel, cats, bullets):
    collisions = pygame.sprite.groupcollide(bullets, cats, True, True)
    if len(cats) == 0:
        bullets.empty()
        create_fleet(game_settings, screen, squirrel, cats)


def create_fleet(game_settings, screen, squirrel, cats):
    cat = Cat(game_settings, screen)
    number_cats_x = get_number_cat_x(game_settings, cat.rect.width)
    number_rows = get_number_rows(game_settings, squirrel.rect.height, cat.rect.height)

    for row_number in range(number_rows):
        for cat_number in range(number_cats_x):
            create_cat(game_settings, screen, cats, cat_number, row_number)


def get_number_cat_x(game_settings, cat_width):
    available_space_x = game_settings.screen_width - 2 * cat_width
    number_cats_x = int(available_space_x / (2 * cat_width))
    return number_cats_x


def get_number_rows(game_settings, squirrel_height, cat_height):
    available_space_y = (game_settings.screen_height - (3 * cat_height) - squirrel_height)
    number_rows = int(available_space_y / (2 * cat_height))
    return number_rows


def create_cat(game_settings, screen, cats, cat_number, row_number):
    cat = Cat(game_settings, screen)
    cat_width = cat.rect.width
    cat.x = cat_width + 2 * cat_width * cat_number
    cat.rect.x = cat.x
    cat.rect.y = cat.rect.height + 2 * cat.rect.height * row_number
    cats.add(cat)


def update_cats(game_settings, stats, screen, squirrel, cats, bullets):
    check_fleet_edges(game_settings, cats)
    cats.update()

    if pygame.sprite.spritecollideany(squirrel, cats):
        squirrel_hit(game_settings, stats, screen, squirrel, cats, bullets)

    check_cats_bottom(game_settings, stats, screen, squirrel, cats, bullets)


def change_fleet_direction(game_settings, cats):
    for cat in cats.sprites():
        cat.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_fleet_edges(game_settings, cats):
    for cat in cats.sprites():
        if cat.check_edges():
            change_fleet_direction(game_settings, cats)
            break


def squirrel_hit(game_settings, stats, screen, squirrel, cats, bullets):
    if stats.lives_left > 0:

        stats.lives_left -= 1
        cats.empty()
        bullets.empty()
        create_fleet(game_settings, screen, squirrel, cats)
        squirrel.center_squirrel()
        sleep(0.5)
    else:
        stats.game_active = False


def check_cats_bottom(game_settings, stats, screen, squirrel, cats, bullets):
    screen_rect = screen.get_rect()
    for cat in cats.sprites():
        if cat.rect.bottom >= screen_rect.bottom:
            squirrel_hit(game_settings, stats, screen, squirrel, cats, bullets)
            break
