import sys
import pygame

from Bullet import Bullet
from cat import Cat


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


def update_screen(game_settings, screen, squirrel, cats, bullets):
    screen.fill(game_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.blitme()

    squirrel.blitme()
    cats.draw(screen)
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


def update_aliens(game_settings, cats):
    check_fleet_edges(game_settings, cats)
    cats.update()


def change_fleet_direction(game_settings, cats):
    for cat in cats.sprites():
        cat.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_fleet_edges(game_settings, cats):
    for cat in cats.sprites():
        if cat.check_edges():
            change_fleet_direction(game_settings, cats)
            break