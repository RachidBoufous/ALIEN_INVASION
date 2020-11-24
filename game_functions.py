import pygame
import sys
from bullet import  Bullet

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

def update_screen(screen,ai_settings,ship,bullets):

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ship.update()
    fire_bullets(bullets)
    remove_old_bullets(bullets)
    pygame.display.flip()


def fire_bullets(bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def remove_old_bullets(bullets):
     for bullet in bullets.copy():
        if bullet.rect.y == 0:
            bullets.remove(bullet)