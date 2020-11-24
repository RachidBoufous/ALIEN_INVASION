import pygame
import sys

from settings import Settings
from ship import Ship
from game_functions import check_events,update_screen
from pygame.sprite import  Group

def run_game():
    """the game main function
    """

    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen,ai_settings)
    bullets = Group()


    pygame.display.set_caption("ALIEN INVASION")
    while True:
        check_events(ship,ai_settings,bullets,screen)
        bullets.update()
        update_screen(screen,ai_settings,ship,bullets )

run_game() 