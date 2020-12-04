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
          self.strategy = DumbStrategy(self.player_num)
          self.state_strat = "Dumb"


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


#Everything from here down was taken from "rand_player"


    def spend_credits(self,game_state):
        decision = self.strategy.decide_purchases(game_state)[0]
        if decision == "Unit Buy":
            self.new_unit(game_state)
        else:
            self.unit_upgrade(game_state)

    def new_unit(self,game_state):
        techs = [
            self.attack_technology, self.defense_technology,
            self.speed_technology
        ]
        for planet in self.Game.planets:
            coords = [planet.coords[0], planet.coords[1]]
            army_choices = [
                [Scout(coords, self, len(self.units), techs), 6, .5],
                [Decoy(coords, self, len(self.units), techs), 1, .5],
                [ShipYard(coords, self, len(self.units), techs), 6, .5],
                [Colony_ship(coords, self, len(self.units), techs), 8, .5],
                [Destroyer(coords, self, len(self.units), techs), 9, 1],
                [Cruiser(coords, self, len(self.units), techs), 12, 1.5],
                [Battlecruiser(coords, self, len(self.units), techs), 15, 2],
                [Battleship(coords, self, len(self.units), techs), 20, 2.5],
                [Dreadnaught(coords, self, len(self.units), techs), 24, 3],
                [Base(coords, self, len(self.units), techs), 0, 1]
            ]
            hull_capacity = 0
            if planet.player_control == self.player_num:
                hull_capacity = planet.ship_yards * self.ship_yard_technology
                choice = self.strategy.decide_purchases(game_state)[1]
                if self.playerCP >= army_choices[choice][
                        1] and hull_capacity >= army_choices[choice][2] * 2:
                    if choice == 9:
                        if planet.base_status == 0:
                            self.units.append(army_choices[choice][0])
                            planet.base_status = 1
                            self.playerCP = self.playerCP - army_choices[
                                choice][1]
                            # print("made unit:" +
                            #       self.units[len(self.units) - 1].name + " " +
                            #       str(len(self.units)))
                            self.Game.board.add_unit_to_board(
                                self.units[len(self.units) - 1],
                                self.player_num)
                    elif choice == 1:
                        chance_for_decoy = random.randint(0, 3)
                        if chance_for_decoy == 2:
                            self.units.append(army_choices[choice][0])
                            self.playerCP = self.playerCP - army_choices[
                                choice][1]
                            # print("made unit:" +
                            #       self.units[len(self.units) - 1].name + " " +
                            #       str(len(self.units)))
                            self.Game.board.add_unit_to_board(
                                self.units[len(self.units) - 1],
                                self.player_num)
                    else:
                        self.units.append(army_choices[choice][0])
                        self.playerCP = self.playerCP - army_choices[choice][1]
                        # print("made unit:" +
                        #       self.units[len(self.units) - 1].name + " " +
                        #       str(len(self.units)))
                        self.Game.board.add_unit_to_board(
                            self.units[len(self.units) - 1], self.player_num)

    def unit_upgrade(self,game_state):
        upgrade_catagory = self.strategy.decide_purchases(game_state)[2]  #0:defense 1:offense 2:speed 3: ship yard

        if upgrade_catagory == 1:  #offense
            if self.attack_technology < 1 and self.playerCP - (
                (self.attack_technology * 10) + 20) >= 0:
                self.playerCP = self.playerCP - (
                    (self.attack_technology * 10) + 20)
                self.attack_technology = self.attack_technology + 1
                print("Player " + str(self.player_num) +
                      ": ^Attack Technology: " +
                      str(self.attack_technology - 1) + "->" +
                      str(self.attack_technology))

        elif upgrade_catagory == 0:  #defense
            if self.defense_technology < 3 and self.playerCP - (
                (self.defense_technology * 10) + 20) >= 0:
                self.playerCP = self.playerCP - (
                    (self.defense_technology * 10) + 20)
                self.defense_technology = self.defense_technology + 1
                print("Player " + str(self.player_num) +
                      ": ^Defense Technology: " +
                      str(self.defense_technology - 1) + "->" +
                      str(self.defense_technology))

        elif upgrade_catagory == 2:  #sped
            if self.speed_technology < 6 and self.playerCP - (
                (self.speed_technology * 10) + 20) >= 0:
                self.playerCP = self.playerCP - (
                    (self.speed_technology * 10) + 20)
                self.speed_technology = self.speed_technology + 1
                print("Player " + str(self.player_num) +
                      ": ^Speed Technology: " +
                      str(self.speed_technology - 1) + "->" +
                      str(self.speed_technology))

        elif upgrade_catagory == 3:  #ship size
            if self.ship_yard_technology < 6 and self.playerCP - (
                (self.ship_yard_technology * 5) + 10) >= 0:
                self.playerCP = self.playerCP - (
                    (self.ship_yard_technology * 5) + 10)
                self.ship_yard_technology = self.ship_yard_technology + 1
                print("Player " + str(self.player_num) +
                      ": ^Ship Size Technology: " +
                      str(self.ship_yard_technology - 1) + "->" +
                      str(self.ship_yard_technology))
