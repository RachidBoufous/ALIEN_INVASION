import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class the module the bullets fired by the ship

    Args:
        Sprite (class): handle the visible obj of thr game
    """

    def __init__(self,ship,settings,screen):
        super().__init__()

        self.ship = ship
        self.settings = settings
        self.screen = screen

        # set the bullet image and get its rect
        self.image = pygame.image.load("images/bullet.png")
        self.rect = self.image.get_rect()

        # position the bullet at the top center of ship
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top


        # get position of the ship alone the y axis
        self.y = float(self.ship.rect.y)

    def update(self):
        """update the postion of the bullet along the y axis
        """
        self.y -= self.settings.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)