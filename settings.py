
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
        self.ship_speed_factor = 1.5

        # ? bullets settings
        self.bullet_speed_factor = 1
        self.bullets_allowed = 5

        # ? alien fleet/ships settings
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 10