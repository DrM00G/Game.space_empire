from players.player import Player
import random
from units.unit import Unit
from units.scout import Scout
from units.destroyer import Destroyer
from units.cruiser import Cruiser
from units.battlecruiser import Battlecruiser
from units.battleship import Battleship
from units.dreadnaught import Dreadnaught
from units.colony_ship import Colony_ship
from units.ship_yard import ShipYard
from units.base import Base
from units.decoy import Decoy




class DumbPlayer(Player):
    def __init__(self,playerCP,player_num,Game,stratagy):
        super().__init__(self,player_num,Game,stratagy)
        self.player_type = "dumb"
        self.playerCP = playerCP
        self.player_num = player_num
        self.defense_technology = 0
        self.attack_technology = 0
        self.speed_technology = 0
        self.ship_yard_technology = 1
        self.Game = Game
        self.dumb_status = stratagy

    def spend_credits(self):
      self.new_unit()


    def new_unit(self):
      techs = [self.attack_technology,self.defense_technology,self.speed_technology]
      for planet in self.Game.planets:
        coords = [planet.coords[0],planet.coords[1]]
        army_choices=[[Scout(coords,self,len(self.units),techs),6,.5]]
        hull_capacity=0
        if planet.player_control == self.player_num:
          hull_capacity = planet.ship_yards*self.ship_yard_technology
          choice = 0
          if self.playerCP >= army_choices[choice][1] and hull_capacity >= army_choices[choice][2]*2:
            self.units.append(army_choices[choice][0])
            self.playerCP = self.playerCP - army_choices[choice][1]
            print("made unit:"+self.units[len(self.units)-1].name+" "+str(len(self.units)))
            self.Game.board.add_unit_to_board(self.units[len(self.units)-1],self.player_num)

