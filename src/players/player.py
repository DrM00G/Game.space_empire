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
from strategies.dumb_strategy import DumbStrategy



class Player:
    def __init__(self, playerCP, player_num, Game, stratagy):
        self.units = []
        self.playerCP = playerCP
        self.player_num = player_num
        self.defense_technology = 0
        self.attack_technology = 0
        self.speed_technology = 0
        self.ship_yard_technology = 1
        self.Game = Game
        if stratagy == "DumbStrategy":
          self.stratagy = DumbStrategy(self.player_num)


    def army_set_up(self, coords):
        techs = [
            self.attack_technology, self.defense_technology,
            self.speed_technology
        ]
        for scout in range(3):
            self.units.append(Scout(coords, self, len(self.units), techs))
        for colon in range(3):
            self.units.append(
                Colony_ship(coords, self, len(self.units), techs))
        for yard in range(4):
            self.units.append(ShipYard(coords, self, len(self.units), techs))

    def get_credits(self, planets):
        for planet in planets:
            if planet.player_control == self.player_num:
                #self.playerCP = self.playerCP + planet.health
                self.playerCP = self.playerCP + 20
                print(str(self.player_num))
                print(self.playerCP)
