import random
from Player import Player
from Planet import Planet



class Game:
    def __init__(self):
        self.turn_numb = 0
        self.winner = None
        self.CP = 20
        self.players = 2
        self.player_coords = [[3,0],[3,6]] 
        self.planets = []

    def generate(self):
        self.players = [Player(self.CP,i + 1) for i in range(2)]
        self.planets = [Planet(coord) for coord in self.player_coords]
        for s in range(2):
            self.players[s].army_set_up(self.player_coords[s])

        possible_coords = [[x,y] for x in range(7) for y in range(7) if x != 3 or (y != 0 and y != 6)]
        for n in range(7):
            choice = random.randrange(len(possible_coords))
            self.planets.append(Planet(possible_coords.pop(choice)))

    def colony_check(self):
      for player in self.players:
        for unit in player.units:
          if unit.name == 'Colony ship' and unit.exist == True:
            for planet in self.planets:
              if planet.colony_status == False:
                if unit.coordinates[0] == planet.coords[0] and unit.coordinates[1] == planet.coords[1]:
                  unit.exist = False
                  planet.colony_status = True
                  planet.player_control = player.PlayerNumb

    def ship_yard_check(self):
      for planet in self.planets:
        if planet.colony_status == True:
          planet.ship_yards = 0
      for player in self.players:
        for unit in player.units:
          if unit.name == 'ShipYard':
            unit.landed= False

      for player in self.players:
        for unit in player.units:
          if unit.name == 'ShipYard' and unit.exist == True:
            for planet in self.planets:
              if planet.colony_status == True and planet.player_control == (self.players.index(player)+1):
                if unit.coordinates[0] == planet.coords[0] and unit.coordinates[1] == planet.coords[1] and planet.ship_yards < 4:
                  planet.ship_yards = planet.ship_yards + 1
                  unit.landed= True



    



    def state(self):
        print("Turn: "+str(self.turn_numb))
        for i in range(len(self.players)):
            print("--------------------------")
            print('Player '+str(i + 1)+':')
            print("CP: "+str(self.players[i].playerCP))
            for unit in self.players[i].units:
                if unit.exist == True:
                  print(""+unit.name+': ('+str(unit.coordinates[0])+","+str(unit.coordinates[1])+")(Unit "+str(unit.unit_number)+")")
        print("--------------------------")


    def unit_v_unit(self,attacker,defender):
      six_roll = random.randint(1, 6)
      if(attacker.strength-defender.defense <= six_roll or six_roll == 1 or defender.name == 'Colony ship' or defender.name == 'Decoy'):
        self.players[self.players.index(defender.player)].units[defender.unit_number-1].armor -= 1
        if self.players[self.players.index(defender.player)].units[defender.unit_number-1].armor <= 0:
          print("Combat at:(" + str(attacker.coordinates[0])+","+str(attacker.coordinates[1])+")")
          print("Player "+ str(self.players.index(attacker.player)+1)+" (Unit " + str(attacker.unit_number) + ") vs Player "+ str(self.players.index(defender.player)+1)+" (Unit " + str(defender.unit_number) + ")")
          defender.exist = False
          print("Survivor: Player "+str(self.players.index(attacker.player)+1)+" (Unit " + str(attacker.unit_number) + ")")

    def complete_turn(self):
        self.turn_numb += 1
        for i in range(len(self.players)):
          self.players[i].get_credits(self.planets)
          self.players[i].decay()
          self.players[i].spend_credits()
        self.ship_yard_check()
        for i in range(len(self.players)):
          for unit in self.players[i].units:
            if unit is not None:
              for j in range(unit.speed):
                if unit.name == 'ShipYard':
                  if unit.landed == False:
                    unit.move()
                else:
                  unit.move()
                
    
    def find_overlap(self):
      coords = []
      for unit in self.players[0].units:
        for unit_compare in self.players[1].units:
            if unit.exist == True and unit_compare.exist == True:
              if unit != unit_compare and unit.coordinates == unit_compare.coordinates:
                coords.append(unit.coordinates)

      for planet in self.planets:
        if planet.colony_status == True:
          for unit in self.players[0].units:
            if unit.coordinates[0] == planet.coords[0] and unit.coordinates[1] == planet.coords[1] and planet.player_control == 2 and unit.exist==True:
              coords.append(unit.coordinates)
          for unit in self.players[1].units:
            if unit.coordinates[0] == planet.coords[0] and unit.coordinates[1] == planet.coords[1] and planet.player_control == 1 and unit.exist==True:
              coords.append(unit.coordinates)

      return coords


    def sort_ships(self):
      order = []
      for n in reversed(range(6)):
        randomizer_list = []
        for player in self.players:
          for unit in player.units:
            if unit.class_num == (n) and unit.exist == True:
              randomizer_list.append([player.units.index(unit),self.players.index(player)])
        for i in range(len(randomizer_list)):
          order.append(randomizer_list.pop(random.randint(0, len(randomizer_list)-1)))
      return(order)

    def resolve_combat(self):
        while len(self.find_overlap()) > 0:
          order = self.sort_ships()
          for attacker in order:
            attacked_check = 0
            if self.players[attacker[1]].units[attacker[0]].coordinates in self.find_overlap() and self.players[attacker[1]].units[attacker[0]].exist == True:
              if self.players[attacker[1]].units[attacker[0]].name != 'Colony ship' and self.players[attacker[1]].units[attacker[0]].name != 'Decoy':
                for defender in self.players[(attacker[1]-1)**2].units:
                  if defender.coordinates == self.players[attacker[1]].units[attacker[0]].coordinates and defender.exist == True:
                    if attacked_check == 0:
                      self.unit_v_unit(self.players[attacker[1]].units[attacker[0]],defender)
                      attacked_check = 1

                if attacked_check == 0:
                  #print("6")
                  for planet in self.planets:
                    if attacker[1]+1 != planet.player_control and planet.colony_status == True:
                      if self.players[attacker[1]].units[attacker[0]].coordinates[0] == planet.coords[0]:
                        if self.players[attacker[1]].units[attacker[0]].coordinates[1] == planet.coords[1]:
                          planet.health = planet.health - 1
                          attacked_check = 1
                          if planet.health == 0:
                            planet.destroy_colony()
          passivist_check = 0
          for unit in order:
            for coord in self.find_overlap():
              if self.players[unit[1]].units[unit[0]].coordinates == coord and (self.players[unit[1]].units[unit[0]].name != 'Colony ship' and self.players[unit[1]].units[unit[0]].name != 'Decoy'):
                passivist_check = 1
                # print(self.players[unit[1]].units[unit[0]].name)
          if passivist_check == 0:
            break


    def show_winner(self):
        print("Turn: "+ str(self.turn_numb))
        for player in self.players:
          print("Player "+str(player.PlayerNumb)+" Techs:")
          print("Defense: "+str(player.defense_technology)+", Attack: "+str(player.attack_technology)+", Speed: "+str(player.speed_technology)+", Ship size: "+str(player.ship_yard_technology))
        print(self.winner)

    def run_to_completion(self):
        while True:
            player1_check = [i for i in self.players[0].units if i.exist is not False]
            player2_check = [i for i in self.players[1].units if i.exist is not False]
            if self.turn_numb >= 200:
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

            self.colony_check()
            self.ship_yard_check()
            self.complete_turn()
            self.resolve_combat()
            self.state()
            self.labeled_scatter_plot()