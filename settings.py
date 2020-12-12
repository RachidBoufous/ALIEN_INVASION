
class Settings():
    """class contains all the settings for the game
    """

    def __init__(self):
        """init the game settings attributes
        """
        # ? main screen surface settings
        self.screen_width = 1400
        self.screen_height = 800

        self.bg_color = (31,31,31)

        # ? player ship settings
        
        self.images = {
            1 : "images/alien1.png",
            2 : "images/alien2.png",
            3 : "images/alien3.png",
            4 : "images/alien4.png",
        }
        self.ship_limit = 3

        # ? bullets settings
        
        self.bullets_allowed = 5

        # ? alien fleet/ships settings
        
        self.fleet_drop_speed = 70

        # ? game_speed scale
        self.speed_up_scale = 1.1

        # game score scale
        self.score_scale = 1.5


        self.re_init_dynamic_settings()
            
    def re_init_dynamic_settings(self):

        self.ship_speed_factor = 3 ##
        self.bullet_speed_factor = 2 ##
        self.alien_speed_factor = 1 ##
        self.fleet_direction = 1 ##
        self.alien_points = 10
    
    def increase_speed(self):
        self.ship_speed_factor  *= self.speed_up_scale
        self.bullet_speed_factor  *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.alien_points *= self.score_scale