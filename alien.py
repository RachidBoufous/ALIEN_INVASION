import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,screen,settings):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("images/alien1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
    
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    
    def check_edges(self):
        if self.rect.right >=self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True

    def update(self):
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)