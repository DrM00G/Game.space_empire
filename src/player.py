from units.colony import Colony
from units.colony_ship import Colonyship
from units.scout import Scout
from units.ship_yard import Shipyard

class Player:
    def __init__(self,p_index,player_strat,init_pos,game):
      self.player_index=p_index
      self.strat=player_strat
      self.home_colony_pos=init_pos
      self.game=game
      self.board=game.board
      self.tech=[0,0,1,1,1]#attk,defn,mov,shpyd,shpsz
      self.units=[Colony(self,0,p_index,self.home_colony_pos,0,self.tech,home_colony=True)]
      self.board.add_to_board(self.units[0])
      self.state_strat=player_strat
      self.CP = 10
      self.set_up_army(self.game.simple)

    def set_up_army(self,simple_army):
      if simple_army:
        for n in range(3):
          self.units.append(Scout(self,n+1,self.player_index,self.home_colony_pos,0,self.tech))
          self.board.add_to_board(self.units[n+1])
        if self.game.level==2:
          for n in range(4):
            self.units.append(Shipyard(self,n+4,self.player_index,self.home_colony_pos,0,self.tech))
            self.board.add_to_board(self.units[n+4])
      else:
        for n in range(3):
          self.units.append(Scout(self,n+1,self.player_index,self.home_colony_pos,0,self.tech))
          self.board.add_to_board(self.units[n+1])
        for n in range(4):
          self.units.append(Shipyard(self,n+4,self.player_index,self.home_colony_pos,0,self.tech))
          self.board.add_to_board(self.units[n+4])
        for n in range(3):
          self.units.append(Colonyship(self,n+8,self.player_index,self.home_colony_pos,0,self.tech))
          self.board.add_to_board(self.units[n+8])

    def movement_phase(self):
      if self.game.simple:
        self.game.move_round=1
        for unit in self.units:
          self.game.movement.move(1, unit,self.game.generate_state())
      else:
        for phase in range(3):
          self.game.move_round=phase+1
          for unit in self.units:
            self.game.movement.move(phase+1, unit,self.game.generate_state())
 



