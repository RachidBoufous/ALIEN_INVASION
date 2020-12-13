from settings import Settings
import pygame
import sys

from bullet import  Bullet
from alien import Alien
from random import randint
from time import sleep

# ? key binding settings

def check_events(ship,settings,bullets,screen,stats,play_button,aliens,sb):

    for event in pygame.event.get():
        check_keydown(event,ship,settings,bullets,screen,stats)
        check_keyup(event,ship)
        mouse_events(event,stats,play_button,aliens,bullets,ship,settings,sb)



def check_keydown(event,ship,settings,bullets,screen,stats):
    """check for the key down events.
    """
    if event.type == pygame.KEYDOWN:
            if stats.game_active:
                if event.key == pygame.K_RIGHT:
                     ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True

            if event.key == pygame.K_SPACE:
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



def mouse_events(event,stats,play_button,aliens,bullets,ship,settings,sb):

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,settings,sb)







# ? screen updates

def update_screen(screen,ai_settings,ship,bullets,
                  aliens,stats,play_game,sb):

    screen.fill(ai_settings.bg_color)


    if not stats.game_active:
        play_game.draw_button()

    else:

        ship.blitme()
        ship.update()

        remove_old_bullets(bullets)
        fire_bullets(bullets)

        aliens.draw(screen)

        sb.draw_score()

    
    pygame.display.flip()



# ? firing bullets mechanism

def fire_bullets(bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def remove_old_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
   

def update_bullets(bullets,aliens,screen,settings,ship,stats,sb):
    bullets.update()
    check_bullet_alien_collisions(bullets,aliens,screen,settings,ship,stats,sb)

def check_bullet_alien_collisions(bullets,aliens,screen,settings,ship,stats,sb):

    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(screen,settings,aliens,ship)
        stats.level +=1
        sb.prep_level()

    if collisions:
        for alien in collisions.values():
            stats.score += settings.alien_points
        sb.prep_score()
        check_high_score(stats,sb)



# ? alien fleet creation

def create_fleet(screen,settings,aliens,ship):
    
    if len(aliens) == 0:
        image_dict = settings.images
        image = image_dict[randint(1,4)]

        alien = Alien(screen,settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        
        number_of_aliens = get_number_of_aliens(settings,alien_width)
        number_of_rows = get_number_of_rows(settings,alien_height,ship)

        for alien_number in range(number_of_aliens):

            for row_number in range(number_of_rows):

                create_alien(screen,settings,alien_width,
                            alien_number,aliens,alien_height,row_number,image)


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


def create_alien(screen,settings,alien_width,alien_number,aliens,alien_height,row_number,image):
        alien = Alien(screen,settings)
        alien.x = alien_width + (2 * alien_width) * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2 * alien_height) * row_number
        alien.image = pygame.image.load(image)
        aliens.add(alien)



# ? aliens_movement_mechanism

def check_fleet_edges(aliens,settings):

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens,settings)
            break

def change_fleet_direction(aliens,settings):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    
    settings.fleet_direction *= -1


def update_aliens(aliens,settings,ship, stats,bullets,sb):
    check_fleet_edges(aliens,settings)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullets,ship,sb)
    
    check_alien_bottom_collision(aliens,stats,bullets,ship,sb)
        


def ship_hit(stats,aliens,bullets,ship,sb):
    if stats.ship_left >= 1:
        
        stats.ship_left -= 1


        ship.center_ship()
        aliens.empty()
        bullets.empty()

        sleep(0.5)
        sb.prep_ships_left()
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

        stats.reset_stats()
        aliens.empty()



def check_alien_bottom_collision(aliens,stats,bullets,ship,sb):
    for alien in aliens.sprites():
        if alien.rect.bottom >= ship.screen_rect.bottom:
            ship_hit(stats,aliens,bullets,ship,sb)
            sb.prep_ships_left()
            break


# ? react to play button 

def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,settings,sb):

    button_clicked_flag = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked_flag and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        settings.re_init_dynamic_settings()
        pygame.mouse.set_visible(False)
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships_left()


def check_high_score(stats,sb):
     
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        write_high_score(stats)
        sb.prep_high_score()


def write_high_score(stats):
    try:
        str_hs = str(stats.high_score)
        with open("game_files/high_score.txt","w") as file_obj:
            file_obj.write(str_hs)
        
    except FileNotFoundError:
        print("file not found")