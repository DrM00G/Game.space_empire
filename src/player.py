from units.colony import Colony
from units.scout import Scout

class Player:
    def __init__(self,p_index,player_strat,init_pos,game):
      self.player_index=p_index
      self.strat=player_strat
      self.home_colony_pos=init_pos
      self.game=game
      self.tech=[0,0,1,1,1]#attk,defn,mov,shpyd,shpsz
      self.units=[Colony(0,p_index,self.home_colony_pos,0,self.tech,home_colony=True)]
      self.state_strat=player_strat
      self.CP = 0
      self.set_up_army()

    def set_up_army(self):
      for n in range(3):
        self.units.append(Scout(len(self.units),self.player_index,self.home_colony_pos,0,self.tech))


