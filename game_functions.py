import pygame
import sys

from bullet import  Bullet
from alien import Alien


def check_events(ship,settings,bullets,screen):
    for event in pygame.event.get():
        check_keydown(event,ship,settings,bullets,screen)
        check_keyup(event,ship)
         


def check_keydown(event,ship,settings,bullets,screen):
    """check for the key down events.
    """
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True

                elif event.key == pygame.K_SPACE:
                    if len(bullets) < settings.bullets_allowed:
                        new_bullet = Bullet(ship,settings,screen)
                        bullets.add(new_bullet)
                elif event.key == pygame.K_q:
                    sys.exit()

def check_keyup(event,ship):
    """check for the key up events
    """
    if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(screen,ai_settings,ship,bullets,aliens):

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ship.update()
    fire_bullets(bullets)
    remove_old_bullets(bullets)
    aliens.draw(screen)
    pygame.display.flip()


def fire_bullets(bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def remove_old_bullets(bullets):
     for bullet in bullets.copy():
        if bullet.rect.y == 0:
            bullets.remove(bullet)




def create_fleet(screen,settings,aliens,ship):

    alien = Alien(screen,settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_of_aliens = get_number_of_aliens(settings,alien_width)
    number_of_rows = get_number_of_rows(settings,alien_height,ship)
    for alien_number in range(number_of_aliens):
        for row_number in range(number_of_rows):
            create_alien(screen,settings,alien_width,
                         alien_number,aliens,alien_height,row_number)


def get_number_of_aliens(settings,alien_width):

    available_space = settings.screen_width - (alien_width * 2)
    number_of_aliens =  int(available_space/(2*alien_width))
    return number_of_aliens

def get_number_of_rows(settings,alien_height,ship):
    available_space_y = (settings.screen_height
                    - (3 * alien_height) -
                    ship.rect.height)
    number_of_rows = int( available_space_y / (2 * alien_height))
    return number_of_rows


def create_alien(screen,settings,alien_width,alien_number,aliens,alien_height,row_number):
        alien = Alien(screen,settings)
        alien.x = alien_width + (2 * alien_width) * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2 * alien_height) * row_number
        aliens.add(alien)

