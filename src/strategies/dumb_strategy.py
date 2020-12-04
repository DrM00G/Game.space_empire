class DumbStratagy:
    def __init__(self,player_num):
        self.player_num = player_num

    def will_colonize_planet(self,colony_ship, game_state):
      return False

    def decide_ship_movement(ship, game_state):
      return [4,None]

    