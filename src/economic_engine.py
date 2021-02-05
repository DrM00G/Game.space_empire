import random
from units.colony import Colony
from units.scout import Scout
from units.ship_yard import Shipyard
from units.destroyer import Destroyer

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
      self.restore_shipyards(player)
      shopping_list=player.strat.decide_purchases(self.game.generate_state())
      self.buy_units(player,shopping_list)
      self.buy_tech(player,shopping_list)
      

    def buy_tech(self, player,shopping_list):
      tech_order=["attack",'defense','movement','shipyard technology',"shipsize"]
      for tech in shopping_list['technology']:
        if self.check_upgrade(tech,player):
          if tech=="attack" or tech=="defense":
            player.cp-=self.game.generate_state['technology_data'][tech][player.tech[tech_order.index(tech)]]
          else:
            player.cp-=self.game.generate_state['technology_data'][tech][player.tech[tech_order.index(tech)]-1]
          player.tech[tech_order.index(tech)]+=1
     


    def check_upgrade(self,tech,player):
      tech_order=["attack",'defense','movement','shipyard technology',"shipsize"]
      if tech=="attack" or tech=="defense":
        if player.tech[tech_order.index(tech)]<len(self.game.generate_state['technology_data'][tech]):
          if player.cp>=self.game.generate_state['technology_data'][tech][player.tech[tech_order.index(tech)]]:
            return True
      else:
        if player.tech[tech_order.index(tech)]-1<len(self.game.generate_state['technology_data'][tech]):
          if player.cp>=self.game.generate_state['technology_data'][tech][player.tech[tech_order.index(tech)]-1]:
            return True
        return False


    def buy_units(self,player,shopping_list):
      for unit in shopping_list["units"]:
        if self.check_for_colony(unit["coords"],player.player_index)!=False:
          builder_colony=self.check_for_colony(unit["coords"],player.player_index)
          if self.check_purchase(player,builder_colony,unit):
            player.cp-=self.game.generate_state()["unit_data"][unit.type]['cp_cost']
            builder_colony.ship_yard_capacity-=self.game.generate_state()["unit_data"][unit.type]['hullsize']
            if unit.type=="Scout":
              player.units.append(Scout(player,len(player.units),player.player_index,unit["coords"],self.game.turn_numb,player.tech))
            elif unit.type=="Shipyard":
              player.units.append(Shipyard(player,len(player.units),player.player_index,unit["coords"],self.game.turn_numb,player.tech))
            elif unit.type=="Destroyer":
              player.units.append(Destroyer(player,len(player.units),player.player_index,unit["coords"],self.game.turn_numb,player.tech))
            self.board.add_to_board(player.units[len(player.units)+1])

    def check_purchase(self,player,colony,unit):
      if self.game.generate_state()["unit_data"][unit.type]['cp_cost']<=player.cp and self.game.generate_state()["unit_data"][unit.type]['hullsize']<=colony.ship_yard_capacity and self.game.generate_state()["unit_data"][unit.type]['shipsize_needed']<=player.tech[4]:
        return True
      else:
        return False

    def check_for_colony(self,coords,player_index):
      for unit in self.board.board_dict[coords]["units"]:
        if unit.name=="Colony" and unit.player_index==player_index:
          return unit
      return False

    def restore_shipyards(self, player):
      for unit in player.units:
        if unit.name=="Colony":
          unit.ship_yard_capacity=unit.calc_shipyards