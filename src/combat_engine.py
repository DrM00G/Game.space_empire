import random


class Combat_Engine:
    def __init__(self, game):
        self.order = []
        self.game = game
        self.players = self.game.players
        self.board = self.game.board

    def sort_ships(self):
        order = []
        for n in reversed(range(6)):
            randomizer_list = []
            for player in self.players:
                for unit in player.units:
                    if unit.class_num == (n) and unit.exist == True:
                        randomizer_list.append([unit, player.player_num])
            for i in range(len(randomizer_list)):
                order.append(randomizer_list.pop(0))
        # print(order)
        return (order)


    def resolve_combat(self,players,test_log):
        self.players = players
        while len(self.game.locate_combat()) > 0:
          order = self.sort_ships()
          conflict_spots = self.game.locate_combat()
          for unit in order:
            for coord in conflict_spots:
              if unit[0].coordinates[0] == coord[0] and unit[0].coordinates[1] == coord[1] and (unit[0].name == 'Colony ship' or unit[0].name == 'Decoy'):
                unit[0].exist = False  
                self.game.boolean_print("Unit "+str(unit[0].unit_number)+": "+unit[0].name+" removed")
          order = self.sort_ships()
          for attacker in order:
            attacked_check = 0

            if attacker[0].coordinates in self.game.locate_combat() and attacker[0].exist == True:
              if attacker[0].name != 'Colony ship' and attacker[0].name != 'Decoy':
                for defender in self.players[(attacker[1]-1)**2].units:
                  if tuple(defender.coordinates) == tuple(attacker[0].coordinates) and defender.exist == True:

                    if attacked_check == 0:
                      self.unit_v_unit(attacker[0],defender,test_log)
                      attacked_check = 1

                if attacked_check == 0:
                  for planet in self.planets:
                    if attacker[1]+1 != planet.player_control and planet.colony_status == True:
                      if attacker[0].coordinates[0] == planet.coords[0]:
                        if attacker[0] == planet.coords[1]:

                          planet.health = planet.health - 1
                          attacked_check = 1
                          if planet.health == 0:
                            planet.destroy_colony()

    def generate_combat_array(self):
      combat_states_arr=[]
      for coords in self.game.locate_combat():
        combat_states_arr.append({'location': coords,'order': [{'player': unit[1], 'unit': unit[2].unit_number} for unit in self.game.board.positions[coords[1]][coords[0]][1]]})
        return(combat_states_arr)

    def combat_state(self):
      for coords in self.game.locate_combat():
        state = {coords:[{'player':[self.board.positions[coords[1]][coords[0]][1][i][1],self.board.positions[coords[1]][coords[0]][1][i][2].unit_number] for i in range(len(self.board.positions[coords[1]][coords[0]][1]))}]for coords in self.game.locate_combat()}
        return state

    def resolve_combat(self, players, test_log):
        self.players = players
        print(self.generate_combat_array())
        while len(self.game.locate_combat()) > 0:
            # print(self.game.locate_combat())
            order = self.sort_ships()
            conflict_spots = self.game.locate_combat()
            for unit in order:
                for coord in conflict_spots:

                    if unit[0].coordinates[0] == coord[0] and unit[
                            0].coordinates[1] == coord[1] and (
                                unit[0].name == 'Colony ship'
                                or unit[0].name == 'Decoy'):
                        unit[0].exist = False
                        self.game.boolean_print(
                            "Unit " + str(unit[0].unit_number) + ": " +
                            unit[0].name + " removed")
            order = self.sort_ships()
            for attacker in order:
                attacked_check = 0

                if list(attacker[0].coordinates) in self.game.locate_combat(
                ) and attacker[0].exist == True:
                    if attacker[0].name != 'Colony ship' and attacker[
                            0].name != 'Decoy':
                        for defender in self.players[1-(attacker[1]-1)**2].units:
                            if tuple(defender.coordinates) == tuple(
                                    attacker[0].
                                    coordinates) and defender.exist == True:

                                if attacked_check == 0:
                                    self.unit_v_unit(attacker[0], defender,
                                                     test_log)
                                    attacked_check = 1

                        if attacked_check == 0:
                            for planet in self.planets:
                                if attacker[
                                        1] + 1 != planet.player_control and planet.colony_status == True:
                                    if attacker[0].coordinates[
                                            0] == planet.coords[0]:
                                        if attacker[0] == planet.coords[1]:

                                            planet.health = planet.health - 1
                                            attacked_check = 1
                                            if planet.health == 0:
                                                planet.destroy_colony()

    def unit_v_unit(self, attacker, defender, test_log):

        if self.game.predetermined_roll == None:
            six_roll = random.randint(1, 6)
        else:
            six_roll = self.game.predetermined_roll[0]
            self.game.predetermined_roll.remove(
                self.game.predetermined_roll[0])
        if (attacker.strength - defender.defense <= six_roll or six_roll == 1
                or defender.name == 'Colony ship' or defender.name == 'Decoy'):
            defender.armor -= 1
            if defender.armor <= 0:
                self.game.boolean_print("Combat at:(" +
                                        str(attacker.coordinates[0]) + "," +
                                        str(attacker.coordinates[1]) + ")")
                self.game.boolean_print(
                    "Player " + str(self.players.index(attacker.player) + 1) +
                    " (Unit " + str(attacker.unit_number) + ") vs Player " +
                    str(self.players.index(defender.player) + 1) + " (Unit " +
                    str(defender.unit_number) + ")")
                defender.exist = False
             
