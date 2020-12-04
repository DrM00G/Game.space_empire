import random
from players.player import Player
from players.dumb_player import DumbPlayer
from players.combat_player import CombatPlayer
from players.rand_player import RandPlayer
from planet import Planet
from board import Board
from combat_engine import Combat_Engine
from movement_engine import MovementEngine
from EconomicEngine import Economic_Engine

class Game:
    def __init__(self,does_print, predetermined_roll = None,planet_amount=9):
        self.predetermined_roll = predetermined_roll
        self.does_print = does_print
        self.turn_numb = 0
        self.winner = None
        self.CP = 0
        self.players = 2
        self.player_coords = [[2, 0], [2, 4]]
        self.planets = []
        self.board = Board()
        self.combat_engine = Combat_Engine(self)
        self.movement_engine = MovementEngine(self)
        self.economic_engine = Economic_Engine(self)
        self.planet_amount=planet_amount



 

    def generate(self):
        self.players = [Player(self.CP,1,self,"DumbStrategy"),Player(self.CP,2,self,"DumbStrategy")]
        self.planets = [Planet(coord,True,self.player_coords.index(coord)+1) for coord in self.player_coords]
        for s in range(2):
            self.players[s].army_set_up(self.player_coords[s])

        possible_coords = [[x,y] for x in range(5) for y in range(5) if x != 2 or (y != 2 and y != 4)]

        for n in range(7):
          choice = possible_coords[random.randrange(len(possible_coords))]
          self.planets.append(Planet(choice,False,0))
        
        self.board.setup(self.planets,self.players)

        

    def add_colonies(self):
      for y in self.board.positions:
        for x in y:
          for planet in x[0]:
            if planet[0] != "Colony":#means theres not a colony there
              for unit in x[1]:
                if unit[0] == "Colony ship":
                  unit[2].exist = False
                  planet[2].colony_status = True
                  planet[2].player_control = unit[1]
                  planet[1] = unit[1]
                  self.boolean_print("Player "+str(planet[2].player_control)+": Creat Colony at "+str(y.index(x))+","+str(self.board.positions.index(y)))
                  planet[0] = "Colony"
                  break
      
      
                  

    def establish_shipyard(self):
      for y in self.board.positions:
        for x in y:
          for planet in x[0]:
            if planet[0] == "Colony":#means theres a colony there
              for unit in x[1]:
                if planet[2].ship_yards < 4:

                  if unit[0] == "ShipYard" and unit[1]==planet[1]:
                    # self.boolean_print("Succses")
                    planet[2].ship_yards = planet[2].ship_yards + 1
                    unit[2].landed = True
                    unit[2].exist = False

      
    def boolean_print(self, str):
      if self.does_print:
        self.boolean_print(str)



    def state(self):
        self.boolean_print("Turn: "+str(self.turn_numb))
        for i in range(len(self.players)):
            self.boolean_print("--------------------------")
            self.boolean_print('Player '+str(i + 1)+':')
            self.boolean_print("CP: "+str(self.players[i].playerCP))
            for unit in self.players[i].units:
                if unit.exist == True:
                  self.boolean_print(""+unit.name+': ('+str(unit.coordinates[0])+","+str(unit.coordinates[1])+")(Unit "+str(unit.unit_number)+")")
        self.boolean_print("--------------------------")

    def movement_phase(self):
        for n in range(3):
          self.boolean_print(" ")
          self.boolean_print("--movement phase: "+str(n)+"--")
          for i in range(len(self.players)):
            for unit in self.players[i].units:
              if unit.exist == True:
                if unit.name == 'ShipYard':
                  if unit.landed == False:
                    self.movement_engine.move(n+1,unit,self.generate_state())
                else:
                  self.movement_engine.move(n+1,unit,self.generate_state())

    def attack_phase(self,test_log):
      self.combat_engine.resolve_combat(self.players,test_log)
      

    def economic_phase(self):
        for i in range(len(self.players)):
            self.economic_engine.get_credits(self.planets,self.players[i])
            self.economic_engine.decay(self.players[i])
            self.players[i].spend_credits(self.generate_state())
        self.add_colonies()
        self.establish_shipyard()

    def complete_turn(self):
        self.turn_numb += 1
        self.boolean_print("----------movement Phase---------")
        self.movement_phase()
        self.boolean_print("--------Combat phase---------")
        self.attack_phase(False)
        self.boolean_print("---------Economic Phase-----------")
        self.economic_phase()

    def generate_state(self):
      state={"Turn":self.turn_numb,
      "Players":[
        {
          "Player Number": player.player_num,
          "CP": player.playerCP,
          "Stratagy": player.state_strat,
          "Units": [
            {"Name": unit.name,
            "Coordinates":unit.coordinates} for unit in player.units
            ]
        } for player in self.players
      ],
      "Planets":[planet.coords for planet in self.planets]
      }
      return state
  
    def locate_combat(self):
        coords = []
        for y in self.board.positions:
            for x in y:
                if len(x[1]) > 1:
                    for unit_index in range(len(x[1]) - 1):
                      for other_unit_index in range(len(x[1]) - 1):
                        if x[1][unit_index][1] != x[1][other_unit_index][1]:
                            if x[1][unit_index][2].exist == True and x[1][other_unit_index][2].exist == True:
                                coords.append([
                                    y.index(x),
                                    self.board.positions.index(y)
                                ])
                elif len(x[1]) + len(x[0]) > 1:
                    for planet in x[0]:
                        if planet[1] != False:
                            for unit in x[1]:
                                if (unit[0] != "Colony ship"
                                        and unit[0] != "ShipYard"
                                        and unit[0] != "Decoy"):
                                    if (planet[1] != unit[1]):
                                        coords.append([
                                            y.index(x),
                                            self.board.positions.index(y)
                                        ])
        return coords

    def show_winner(self):
        self.boolean_print("Turn: " + str(self.turn_numb))
        for player in self.players:
            self.boolean_print("Player " + str(player.player_num) + " Techs:")
            self.boolean_print("Defense: " + str(player.defense_technology) +
                               ", Attack: " + str(player.attack_technology) +
                               ", Speed: " + str(player.speed_technology) +
                               ", Ship size: " +
                               str(player.ship_yard_technology))
        
  
    def locate_combat(self):
      coords = []

      for y in self.board.positions:
        for x in y:
          if len(x[1]) > 1:
            for unit_index in range(len(x[1])-1):
                if x[1][unit_index][1] != x[1][unit_index+1][1]:
                  if x[1][unit_index][2].exist == True and x[1][unit_index+1][2].exist == True:

                    coords.append([y.index(x),self.board.positions.index(y)])
          elif len(x[1])+len(x[0])>1:
            for planet in x[0]:
              if planet[1] != False:
                for unit in x[1]:
                  if(unit[0] != "Colony ship" and unit[0] != "ShipYard" and unit[0] != "Decoy"):
                    if(planet[1] != unit[1]):
                      # self.boolean_print("1")
                      coords.append([y.index(x),self.board.positions.index(y)])
      return coords


   


    def show_winner(self):
        self.boolean_print("Turn: "+ str(self.turn_numb))
        for player in self.players:
          self.boolean_print("Player "+str(player.player_num)+" Techs:")
          self.boolean_print("Defense: "+str(player.defense_technology)+", Attack: "+str(player.attack_technology)+", Speed: "+str(player.speed_technology)+", Ship size: "+str(player.ship_yard_technology))
        self.boolean_print(self.winner)

    def run_to_completion(self, round_limit):
        self.establish_shipyard()
        while True:
            player1_check = [
                i for i in self.players[0].units if i.exist is not False
            ]
            player2_check = [
                i for i in self.players[1].units if i.exist is not False
            ]
            player1_check = [i for i in self.players[0].units if i.exist is not False]
            player2_check = [i for i in self.players[1].units if i.exist is not False]
            if self.turn_numb >= round_limit:
                if len(player1_check) > len(player2_check):
                    self.winner = "Winner: Player 1 (out of moves)"
                elif len(player1_check) < len(player2_check):
                    self.winner = "Winner: Player 2 (out of moves)"
                else:
                    self.winner = "Tie"
                break
            if len(player1_check) == 0:
                self.winner = "Winner: Player 2"
                break
            if len(player2_check) == 0:
                self.winner = "Winner: Player 1"
                break

            self.complete_turn()
            self.state()
