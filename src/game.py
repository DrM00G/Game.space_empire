from combat_engine import CombatEngine
from movement_engine import MovementEngine
from economic_engine import EconomicEngine
from planet import Planet
from board import Board
from logger import Logger

# logging.basicConfig(filename="logs/level2_logs.log",
#                     format='%(message)s',
#                     filemode='w')


class Game:
    def __init__(self, board_size=[5, 5], die_mode="random", sided_die=10, simple=False, level=1, log=True, log_name="logs"):
        self.level = level
        self.simple = simple
        self.board_size = board_size
        self.die_mode = die_mode
        self.planet_nums = 0
        self.board = Board(self.board_size)
        self.players = []
        self.turn_numb = 1
        self.phase = None
        self.logger = Logger(log_name, log)
        self.move_round = 0
        self.planets = []
        self.winner = None
        self.player_whose_turn = None
        self.combat = CombatEngine(die_mode, sided_die, self.board, self)
        self.movement = MovementEngine(self.board)
        self.economy = EconomicEngine(self, self.board)

    def log(self, string):
        if self.logger is not None:
            self.logger.log(string)

    def setup(self, players):
        self.players = players
        for player in players:
            self.planets.append(Planet(player.home_colony_pos, colony=True))
            self.board.board_dict[player.home_colony_pos]["planet"] = self.planets[len(
                self.planets)-1]

    def economic_phase(self):
        self.phase = "Economic"
        self.log(str(self.phase)+str(self.turn_numb))
        for player in self.players:
            self.economy.complete_economic_phase(player)

    def movement_phase(self):
        self.phase = "Movement"
        self.log("")
        self.log("BEGINNING OF TURN "+str(self.turn_numb)+" MOVEMENT PHASE")
        self.log("")

        self.move_round = 0
        if self.level < 3:
            self.move_round = 1
            for player in self.players:
                player.movement_phase(1)
        else:
            for phase in range(3):
                self.move_round = phase+1
                if self.move_round != 1:
                    self.log("")
                self.log("Movement Round "+str(self.move_round))
                for player in self.players:
                    player.movement_phase(phase+1)

        self.log("")
        self.log("Ending Unit Locations")
        self.log("")
        for player in self.players:
            for unit in player.units:
                self.log("Player "+str(player.player_index)+" " +
                         unit.name+" "+str(unit.unit_index)+": "+str(unit.coords))
        self.log("")
        self.log("END OF TURN "+str(self.turn_numb)+" MOVEMENT PHASE")
        self.log("")

    def combat_phase(self):
        self.phase = "Combat"
        self.log("")
        self.log("BEGINNING OF TURN "+str(self.turn_numb)+" COMBAT PHASE")
        self.log("")
        self.combat.complete_combat_phase()
        self.log("")
        self.log("END OF TURN "+str(self.turn_numb)+" COMBAT PHASE")
        self.log("")

    def choose_winner(self, loser):
        # print("Winner is Player"+str(abs(loser-1)))
        self.winner = abs(loser-1)
        # self.combat_phase().exit()
        # self.run_until_winner().exit()

    def run_until_winner(self):
        if self.level == 2:
            self.economic_phase()

        while self.winner == None:
            # print("Move")

            self.movement_phase()

            # self.log(self.board.board_dict)
            # print("Fight")
            self.combat_phase()
            if self.level >= 3 and self.winner == None:
                self.economic_phase()
            # if self.turn_numb>50:
            #   print(self.board.board_dict)
            print(self.turn_numb)
            self.turn_numb += 1
            if self.turn_numb > 5:
                self.winner = 2
        self.log("Winner: "+str(self.winner))
        self.logger.close_file()
        return self.winner

    def generate_state(self):
        state = {"turn": self.turn_numb,
                 'phase': self.phase,  # Can be 'Movement', 'Economic', or 'Combat'
                 'board_size': self.board_size,
                 'round': self.move_round,  # if the phase is movement, then round is 1, 2, or 3
                 # index of player whose turn it is (or whose ship is attacking during battle),
                 'player_whose_turn': self.player_whose_turn,
                 'winner': None,
                 'players': [
                     {
                         'home_coords': player.home_colony_pos,
                         "player_num": player.player_index,
                         "cp": player.CP,
                         "Stratagy": player.state_strat,
                         "units": [
                             unit.state() for unit in player.units if unit.exists],
                         'technology': {'attack': player.tech[0], 'defense': player.tech[1], 'movement': player.tech[2], 'shipyard technology':player.tech[3], 'shipsize': player.tech[4]}
                     } for player in self.players
                 ],
                 "planets": [planet.coords for planet in self.planets], 'unit_data': {
                     'Battleship': {'cp_cost': 20, 'hullsize': 3, 'shipsize_needed': 5, 'tactics': 5, 'attack': 5, 'defense': 2, 'maintenance': 3},
                     'Battlecruiser': {'cp_cost': 15, 'hullsize': 2, 'shipsize_needed': 4, 'tactics': 4, 'attack': 5, 'defense': 1, 'maintenance': 2},
                     'Cruiser': {'cp_cost': 12, 'hullsize': 2, 'shipsize_needed': 3, 'tactics': 3, 'attack': 4, 'defense': 1, 'maintenance': 2},
                     'Destroyer': {'cp_cost': 9, 'hullsize': 1, 'shipsize_needed': 2, 'tactics': 2, 'attack': 4, 'defense': 0, 'maintenance': 1},
                     'Dreadnaught': {'cp_cost': 24, 'hullsize': 3, 'shipsize_needed': 6, 'tactics': 5, 'attack': 6, 'defense': 3, 'maintenance': 3},
                     'Scout': {'cp_cost': 6, 'hullsize': 1, 'shipsize_needed': 1, 'tactics': 1, 'attack': 3, 'defense': 0, 'maintenance': 1},
                     'Shipyard': {'cp_cost': 3, 'hullsize': 0, 'shipsize_needed': 1, 'tactics': 3, 'attack': 3, 'defense': 0, 'maintenance': 0},
                     'Decoy': {'cp_cost': 1, 'hullsize': 0, 'shipsize_needed': 1, 'tactics': 0, 'attack': 0, 'defense': 0, 'maintenance': 0},
                     'Colonyship': {'cp_cost': 8, 'hullsize': 1, 'shipsize_needed': 1, 'tactics': 0, 'attack': 0, 'defense': 0, 'maintenance': 0},
                     'Base': {'cp_cost': 12, 'hullsize': 3, 'shipsize_needed': 2, 'tactics': 5, 'attack': 7, 'defense': 2, 'maintenance': 0}
                 },
                 'technology_data': {
                     'shipsize': [10, 15, 20, 25, 30],
                     'attack': [20, 30, 40],
                     'defense': [20, 30, 40],
                     'movement': [20, 30, 40, 40, 40],
                     'shipyard': [20, 30]
                 }
                 }
        return state
