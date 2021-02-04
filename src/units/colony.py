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

    def destroy_colony(self):
        self.exists = False
        for unit in self.assets:
          unit.exists=False

    def destroy(self)
        if self.home_colony:
          self.player.game.choose_winner(loser=self.player_index)