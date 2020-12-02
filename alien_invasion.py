import pygame
import sys

from settings import Settings
from ship import Ship
from game_functions import check_events,update_screen,create_fleet
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
    create_fleet(screen,ai_settings,aliens,ship)
    while True:
        check_events(ship,ai_settings,bullets,screen)
        bullets.update()
        update_screen(screen,ai_settings,ship,bullets,aliens)

run_game() 