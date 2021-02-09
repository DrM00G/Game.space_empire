from units.unit import Unit

class Colony(Unit):
    def __init__(self,player,unit_index,p_index,init_coords,turn_bought,tech,home_colony=False):
        super().__init__(player,unit_index,p_index,init_coords,turn_bought)
        self.can_move=False
        self.attack = 0
        self.defense = 1
        self.tactics = 0
        self.movement = 0
        self.armor = 3
        self.name = 'Colony'
        self.combat_ready = True
        self.home_colony=home_colony
        self.assets=[]
        self.ship_yard_capacity=0

    def destroy_colony(self):
        for unit in self.assets:
          unit.exists=False

    def destroy(self):
        if self.home_colony:
          self.player.game.choose_winner(loser=self.player_index)
        self.exists=False
        self.player.board.remove_from_board(self)
        self.destroy_colony()

    def calc_shipyards(self):
      spyd_count=0
      for unit in self.assets:
        if unit.name=="Shipyard":
          spyd_count+=unit.spyd_tech
      return spyd_count
