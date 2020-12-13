import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():

    def __init__(self,screen,settings,stats):

        self.screen = screen
        self.stats = stats
        self.settings = settings
        
        self.screen_rect = self.screen.get_rect()
        
        self.txt_color = (230, 13, 44)
        self.bg_color = self.settings.bg_color
        self.font = pygame.font.SysFont(None,48)


        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships_left()
    
    def prep_score(self):
        rounded_score = int(round(self.stats.score,-1))

        score_str = "{:,}".format(rounded_score)
        
        self.score_img = self.font.render(score_str,True,
                                         self.txt_color,
                                         self.bg_color)
        self.score_rect = self.score_img.get_rect()

        # position the rect
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.y = 20


    def prep_high_score(self):

        high_score = int(round(self.stats.high_score,-1))
        hs_str = "{:,}".format(high_score)
        final_str = "highscore: " + hs_str
        self.sh_img = self.font.render(final_str,True,self.txt_color,self.bg_color)

        self.sh_rect = self.sh_img.get_rect()
        self.sh_rect.right = self.screen_rect.right - 20
        self.sh_rect.top = 20

    def prep_level(self):
        level = "lvl: " + str(self.stats.level)
        self.lvl_img = self.font.render(level,True,self.txt_color,self.bg_color)

        self.lvl_rect =self.lvl_img.get_rect()
        self.lvl_rect.right = self.screen_rect.right - 20
        self.lvl_rect.bottom = self.screen_rect.bottom

    def prep_ships_left(self):

        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen,self.settings)
            ship.rect.x = 10 + ship_number * (ship.rect.width / 2)
            ship.rect.y = 20
            ship.image = pygame.image.load("images/heart.png")
            self.ships.add(ship)

    def draw_score(self):
        self.screen.blit(self.score_img,self.score_rect)
        self.screen.blit(self.sh_img,self.sh_rect)
        self.screen.blit(self.lvl_img,self.lvl_rect)
        self.ships.draw(self.screen)