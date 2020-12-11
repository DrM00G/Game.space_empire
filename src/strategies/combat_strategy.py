class CombatStrategy:
    def __init__(self,player_num):
        self.player_num = player_num
        self.next_buy = 'Destroyers'

    def will_colonize_planet(self,colony_ship, game_state):
      return False

    def decide_ship_movement(self,ship, game_state):
      if ship.coordinates[1]<2:
        return "Up"
      elif ship.coordinates[1]>2:
        return "Down"
      if ship.coordinates[0]<2:
        return "Right"
      elif ship.coordinates[1]>2:
        return "Left"
      else:
        return"Stay"


    def decide_purchases(self,game_state):
      if game_state['Players'][self.player_num-1]['Technology']['Ship Size Technology']>2:
        return["Upgrade",3]
      elif self.next_buy == 'Destroyers':
        self.next_buy = 'Scout'
        return["Unit Buy",4]
      elif self.next_buy == 'Scout':
        self.next_buy = 'Destroyers'
        return["Unit Buy",0]

    def decide_which_ship_to_attack(attacking_ship, game_state):
      return 'highest'#REFACTOR