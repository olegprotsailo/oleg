import pygame
from pygame.sprite import Sprite
class Alien (Sprite) :
    def __init__(self,screen,game_settings):
        super (). __init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image,self.rect)

