import pygame

class Ship():
    """class that module the ship
    """

    def __init__(self,screen,ai_settings):
        """init the attribute for the ship class

        Args:
            screen (surface): main game's surface
            ai_settings (class): main game's settings
        """

        self.settings = ai_settings
        # load the screen surface and the ship image.
        self.screen = screen
        self.image = pygame.image.load('images/fighter2.png')

        # get the rects of image and screen surfaces
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # place the ship at the center bottom of the screen surface 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # allow continuouse movement when holding left-right keys
        self.moving_right = False
        self.moving_left = False

        # speed factor of the ship
        self.speed_factor = self.settings.ship_speed_factor
        
        self.x = float(self.rect.centerx)


    def update(self):
        """allow the ship to move as long as left-right keys are in hold
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
             self.x -= self.speed_factor

        self.rect.centerx = self.x

    def blitme(self):
        """draw the ship on screen surface
        """
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        self.x = self.screen_rect.centerx