import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,gamesettings,screen,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,gamesettings.bullet_width,gamesettings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed=gamesettings.bullet_speed_factor
        self.color = gamesettings.bullet_color
    def update(self,):
        self.rect.y-=self.speed
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
