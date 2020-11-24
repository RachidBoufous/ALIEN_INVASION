
class Settings():
    """class contains all the settings for the game
    """

    def __init__(self):
        """init the game settings attributes
        """
        self.screen_width = 1400
        self.screen_height = 800

        self.bg_color = (31,31,31)


        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullets_allowed = 5
