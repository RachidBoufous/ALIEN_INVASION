import pygame
import sys

from settings import Settings
from ship import Ship
from game_functions import (check_events,
                            update_screen,
                            create_fleet,
                            update_bullets,
                            update_aliens)
from pygame.sprite import  Group


def run_game():
    """the game main function
    """

    pygame.init()

    pygame.display.set_caption("ALIEN INVASION")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen,ai_settings)
    bullets = Group()

    aliens = Group()
    
    while True:
        if len(aliens) == 0:
            create_fleet(screen,ai_settings,aliens,ship)
        check_events(ship,ai_settings,bullets,screen)
        update_bullets(bullets,aliens)
        update_aliens(aliens,ai_settings)
        update_screen(screen,ai_settings,ship,bullets,aliens)

run_game() 