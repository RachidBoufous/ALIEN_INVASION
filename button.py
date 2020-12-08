import pygame.font
import pygame

class Button():

    def __init__(self,screen,msg):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200,50
        self.bg_color = (39, 40, 34)
        self.txt_color = (236, 39, 47)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep(msg)


    def prep(self,msg):
        """render an image frm a given text.

        Args:
            msg (string): txt to be rendered
        """

        self.msg_image = self.font.render(msg,True,self.txt_color,self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        """fill the button, then blit the text on it
        """

        self.screen.fill(self.bg_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)