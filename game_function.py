import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


def check_events(gamesettings,screen,ship, bullets):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            check_keydown_events(gamesettings,screen,ship, i, bullets)

        elif i.type == pygame.KEYUP:
            check_keyup_events(i, ship)

def check_keydown_events(game_settings,screen,ship, i, bullets):
    if i.key == pygame.K_RIGHT:
        ship.moving_right = True
    if i.key == pygame.K_LEFT:
        ship.moving_left = True
    if i.key == pygame.K_UP:
        ship.moving_up = True
    if i.key == pygame.K_DOWN:
        ship.moving_down = True
    if i.key == pygame.K_SPACE:
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)
def check_keyup_events(i, ship):
    if i.key == pygame.K_RIGHT:
        ship.moving_right = False
    if i.key == pygame.K_LEFT:
        ship.moving_left = False
    if i.key == pygame.K_UP:
        ship.moving_up = False
    if i.key == pygame.K_DOWN:
        ship.moving_down = False





def update_screen(screen,ship,game_settings,bullets, background, aliens):

    background.update()
    #screen.fill(game_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(bullets):

    for bullet in bullets.copy ():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet (game_settings,screen,aliens):
    alien = Alien(game_settings,screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2* alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(game_settings,screen)
        alien.x = alien_width +2* alien_width * alien_number
        alien.rect.x = alien_width
        alien.add(aliens)
def get_number_rows(game_settings,ship_height,alien_hight):
    available_space_y = game_settings.screen_height - (8 * alien_hight) - ship_height
    number_rows = int(available_space_y / (2*alien_hight))
    return (number_rows)
def create_alien (game_settings,screen,aliens,alien_number,row_number):
    alien = Alien(game_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height +2*alien.rect.height * row_number
    aliens.add(alien)
def create_fleet (game_settings,screen,aliens,ship):
    alien = Alien(game_settings,screen)
    number_aliens_x = get_number_aliens_x (game_settings,alien.rect.width)
    number_rows = get_number_rows(game_settings,ship.rect.height,alien.rect.height)
    for row_number in range (number_rows):
        for alien_number in range (number_aliens_x):
            create_alien(game_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(game_settings,alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2 *alien_width))
    return (number_aliens_x)




