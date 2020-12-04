class DumbStrategy:
    def __init__(self,player_num):
        self.player_num = player_num

    def will_colonize_planet(self,colony_ship, game_state):
      return False

    def decide_ship_movement(self,ship, game_state):
      return [4,None]

    def decide_purchases(self,game_state):
      return["Unit Buy",0]#referance the "army_choices" int in player to see what number is what. IF OTHER OPTIONS, RETURN WITH A RANDOM. IF TECH COULD BE UPGRADED, IT WOULD BE LAST POSITION