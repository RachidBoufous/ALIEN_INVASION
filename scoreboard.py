import pygame.font


class Scoreboard():

    def __init__(self,screen,settings,stats):

        self.screen = screen
        self.stats = stats
        self.screen_rect = self.screen.get_rect()
        
        self.txt_color = (230, 13, 44)
        self.bg_color = settings.bg_color
        self.font = pygame.font.SysFont(None,48)


        self.prep_score()

    
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

    
    def draw_score(self):
        self.screen.blit(self.score_img,self.score_rect)