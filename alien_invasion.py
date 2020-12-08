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
from game_stats import Game_Stats


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
    stats = Game_Stats(ai_settings)

    while True:
        check_events(ship,ai_settings,bullets,screen,stats)
        if stats.game_active:
            create_fleet(screen,ai_settings,aliens,ship)
            update_bullets(bullets,aliens)
            update_aliens(aliens,ai_settings,ship,stats,bullets)
        update_screen(screen,ai_settings,ship,bullets,aliens)

run_game() 