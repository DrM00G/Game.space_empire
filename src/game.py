import random
from combat_engine import CombatEngine
from movement_engine import MovementEngine
from economic_engine import EconomicEngine
from planet import Planet
from board import Board
import logging 
  
logging.basicConfig(filename="logs/level2_logs.log", 
                    format='%(message)s', 
                    filemode='w') 


class Game:
    def __init__(self,board_size=[5,5],die_mode="random",sided_die=10, simple=False,level=1):
      self.level=level
      self.simple=simple
      self.board_size=board_size
      self.die_mode=die_mode
      self.planet_nums=0
      self.board=Board(self.board_size)
      self.players=[]
      self.turn_numb=1
      self.phase = None
      self.logger=logging.getLogger() 
      self.logger.setLevel(logging.DEBUG) 
      self.move_round=0
      self.planets=[]
      self.winner=None
      self.player_whose_turn= None
      self.combat = CombatEngine(die_mode,sided_die,self.board,self)
      self.movement = MovementEngine(self.board)
      self.economy = EconomicEngine(self,self.board)
      

    def setup(self,players):
      self.players=players
      for player in players:
        self.planets.append(Planet(player.home_colony_pos,colony=True))
        self.board.board_dict[player.home_colony_pos]["planet"]=self.planets[len(self.planets)-1]

    def economic_phase(self):
        self.phase="Economic"
        self.logger.info(str(self.phase)+str(self.turn_numb))
        for player in self.players:
          self.economy.complete_economic_phase(player)

    def movement_phase(self):
        self.phase="Movement"
        self.logger.info(str(self.phase)+str(self.turn_numb))
        for player in self.players:
          player.movement_phase()

    def combat_phase(self):
        self.phase="Combat"
        self.logger.info(str(self.phase)+str(self.turn_numb))
        self.combat.complete_combat_phase()

    def choose_winner(self,loser):
        # print("Winner is Player"+str(abs(loser-1)))
        self.winner=abs(loser-1)
        # self.combat_phase().exit()
        # self.run_until_winner().exit()

    def run_until_winner(self):
      if self.level==2:
        self.economic_phase()
      
      while self.winner == None:
        # print("Move")
        for coord in self.board.board_dict:
          if len(self.board.board_dict[coord]["units"])>0:
            self.logger.info(str(coord)+":"+str([str(unit.name)+str(unit.unit_index)+"["+str(unit.player_index)+"]" for unit in self.board.board_dict[coord]["units"]]))
        self.movement_phase()
        # self.logger.info(self.board.board_dict)
        # print("Fight")
        self.combat_phase() 
        if self.level>=3:
          self.economic_phase()         
        # if self.turn_numb>50:
        #   print(self.board.board_dict)
        self.turn_numb+=1
        if self.turn_numb>100:
          self.winner=2
      self.logger.info("Winner: "+str(self.winner))
      return self.winner

    def generate_state(self):
        state={"turn":self.turn_numb,
          'phase': self.phase, # Can be 'Movement', 'Economic', or 'Combat'
          'board_size': self.board_size,
          'round': self.move_round, # if the phase is movement, then round is 1, 2, or 3
          'player_whose_turn': self.player_whose_turn, # index of player whose turn it is (or whose ship is attacking during battle),
          'winner': None,
          'players': [
            {
          'home_coords': player.home_colony_pos,
          "player_num": player.player_index,
          "cp": player.CP,
          "Stratagy": player.state_strat,
          "units": [
            {"type": unit.name,
            "unit_num":unit.unit_index,
            "coords":unit.coords,
            "technology":{"defense": unit.defense,"attack": unit.attack,"movement": unit.movement},
            "hits_left":unit.armor,
            'turn_created':unit.turn_made,
            'exists':unit.exists
            }for unit in player.units if unit.exists],
            'technology': {'attack': player.tech[0], 'defense': player.tech[1], 'movement': player.tech[2],'shipyard technology':player.tech[3], 'shipsize': player.tech[4]}
            } for player in self.players
            ],
          "planets":[planet.coords for planet in self.planets],'unit_data': {
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