import pygame
import sys

from settings import Settings
from ship import Ship
from game_functions import (check_events,
                            update_screen,
                            create_fleet,
                            update_bullets,
                            update_aliens,
                            )
from pygame.sprite import  Group
from game_stats import Game_Stats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """the game main function
    """
    
    pygame.init()
    pygame.display.set_caption("ALIEN INVASION")
    
    # > vars declarition goes here

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    bullets = Group()
    aliens = Group()

    ship = Ship(screen,ai_settings)
    stats = Game_Stats(ai_settings)
    play_button = Button(screen,"PLAY")
    sb = Scoreboard(screen,ai_settings,stats)

    
    

    while True:

        check_events(ship,ai_settings,bullets,screen,stats,play_button,aliens,sb)

        if stats.game_active:

            create_fleet(screen,ai_settings,aliens,ship)
            update_bullets(bullets,aliens,screen,ai_settings,ship,stats,sb)
            update_aliens(aliens,ai_settings,ship,stats,bullets)


        update_screen(screen,ai_settings,ship,bullets,aliens,stats,play_button,sb)

run_game()