import random

class EconomicEngine:
    def __init__(self,game,board):
      self.board=board
      self.game=game

    def complete_economic_phase(self,player):
      self.get_cp(player.units)
      self.maintnance(player.units,player)
      self.buy_stuff(player)

    def get_cp(self,units):
      for unit in units:
        if unit.exists:
          if unit.name == "Colony":
            if unit.home_colony:
              unit.player.cp+=20
            else:
              unit.player.cp+=5

    def maintnance(self,units,player):
      cp_tally=0
      for unit in units:
        if unit.exists:
          if unit.name != "Colony":
            cp_tally+=self.game.generate_state()["unit_data"]['maintenance']
      if cp_tally<=player.cp:
        player.cp-=cp_tally
      else:
        self.remove_unit(player.strat.decide_removal(self.game.generate_state()),units)
        self.maintnance(units,player)

    def remove_unit(self,removal_index,units):
      self.board.remove_from_board(units[removal_index])

    def buy_stuff(self,player):
      shopping_list=player.strat.decide_purchases(self.game.generate_state())
      for unit in shopping_list["units"]:
        if
        

    def check_for_colony(self,coords,player_index):
      for units in self.board.board_dict[coords]["units"]:
        