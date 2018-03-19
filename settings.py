import pygame
import sys
class Settings():
    def __init__(self):
        self.screen_width = 1830
        self.screen_height = 1200
        self.bg_color = (43,64,12)

        self.bullet_width = 20
        self.bullet_height = 15
        self.bullet_color = (23,50,23)
        self.bullet_speed_factor=10
        self.bullets_allowed = 2