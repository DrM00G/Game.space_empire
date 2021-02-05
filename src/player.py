from units.colony import Colony
from units.scout import Scout

class Player:
    def __init__(self,p_index,player_strat,init_pos,game,simple_army=False):
      self.player_index=p_index
      self.strat=player_strat
      self.home_colony_pos=init_pos
      self.game=game
      self.board=game.board
      self.tech=[0,0,1,1,1]#attk,defn,mov,shpyd,shpsz
      self.units=[Colony(self,0,p_index,self.home_colony_pos,0,self.tech,home_colony=True)]
      self.state_strat=player_strat
      self.CP = 0
      self.set_up_army(simple_army)

    def set_up_army(self,simple_army):
      for n in range(3):
        self.units.append(Scout(self,n+1,self.player_index,self.home_colony_pos,0,self.tech))
        self.board.add_to_board(self.units[n+1])

    def movement_phase(self):
      for phase in range(3):
        self.game.move_round=phase+1
        for unit in self.units:
          self.game.movement.move(phase+1, unit,self.game.generate_state())
 



