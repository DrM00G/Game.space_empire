import random
from players.player import Player

class Game:
    def __init__(self,board_size=[5,5],die_mode="random"):
      self.board_size=board_size
      self.die_mode=die_mode
      self.planet_nums=0
      self.players=[]
      self.combat = CombatEngine(self,die_mode)
      self.movement = MovementEngine(self)
      self.economy = EconomicEngine(self)
      

    def setup(self,player_strats,innit_pos):
      for p_index in range(len(player_strats)):
        self.players.append(Player(p_index,player_strats[p_index],innit_pos[p_index],Game=self))



    