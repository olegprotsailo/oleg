import pygame
import sys
class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images/ashot.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.moving_right=False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.shoot = False
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right :
            self.rect.centerx += 10
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx -= 10
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.rect.centery -= 10
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery += 10
