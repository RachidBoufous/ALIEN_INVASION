
class Game_Stats():

    def __init__(self,settings):

        self.settings = settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.get_high_score()

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
        
    def get_high_score(self):
        str_hs = ""
        with open("game_files/high_score.txt","r") as file_obj:
            str_hs = file_obj.read()
        
        return int(str_hs)