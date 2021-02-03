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


class DavidStrategyPlayer(Player):
    def __init__(self, playerCP, player_num, Game, dumb):
        super().__init__(self, player_num, Game, dumb)
        self.player_type = "Stratagy"
        self.playerCP = playerCP
        self.player_num = player_num
        self.defense_technology = 0
        self.attack_technology = 0
        self.speed_technology = 0
        self.ship_yard_technology = 1
        self.game = Game
        self.dumb_status = dumb

def calc_distance(coords_1, coords_2):
    x_1, y_1 = coords_1
    x_2, y_2 = coords_2
    return abs(x_2 - x_1) + abs(y_2 - y_1)

def will_colonize_planet(colony_ship, planet, game):
    for planet in game.planets:
      distance=self.calc_distance(planet.coordinates, unit.coordinates)
      if unit.name = "Colony_ship" and distance==0 and planet.colonizer = "Uncolonized":
        return True
      else:
        return False


def Player.decide_ship_movement(ship, game):
    if ship.name="Colony_Ship":
      for planet in game.planets:
        if planet.colonizer = "Uncolonized"
          if ship.coordinates[0]>planet.coordinates[0]:
            ship.coordinates[0]=+1
          elif ship.coordinates[0]<planet.coordinates[0]:
            ship.coordinates[0]=-1
          elif ship.coordinates[1]<planet.coordinates[1]:
            ship.coordinates[1]=-1
          elif ship.coordinates[1]>planet.coordinates[1]:
            ship.coordinates[1]=+1
    else:
      for planet in game.planets:
        if planet.colonizer != ship.player_num:
          if ship.coordinates[0]>planet.coordinates[0]:
            ship.coordinates[0]=+1
          elif ship.coordinates[0]<planet.coordinates[0]:
            ship.coordinates[0]=-1
          elif ship.coordinates[1]<planet.coordinates[1]:
            ship.coordinates[1]=-1
          elif ship.coordinates[1]>planet.coordinates[1]:
            ship.coordinates[1]=+1