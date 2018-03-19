import pygame
import sys
from settings import Settings
from ship import Ship
from alien import Alien
import game_function
from pygame.sprite import Group
from background import Background

def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height,))
    #bg_color = (game_settings.bg_color)
    pygame.display.set_caption("Ship")
    ship = Ship(screen)
    bullets=Group( )
    background = Background(screen)
    aliens = Group()


    game_function.create_fleet(game_settings,screen,aliens, ship)
    while True:
        game_function.check_events(game_settings,screen,ship, bullets)
        game_function.update_screen(screen,ship,game_settings,bullets, background, aliens)
        ship.update()
        bullets.update()
        game_function.update_bullets(bullets)
        background.update ()
        print(len(bullets))


init_game()