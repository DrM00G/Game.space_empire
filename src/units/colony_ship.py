from units.unit import Unit

class Colonyship(Unit):
    def __init__(self,player,unit_index,p_index,init_coords,turn_bought,tech):
        super().__init__(player,unit_index,p_index,init_coords,turn_bought)
        self.can_move=True
        self.attack = 0
        self.defense = 0 
        self.tactics = 0
        self.movement = tech[2]
        self.armor = 2
        self.name = 'Colony Ship'
        self.combat_ready = False
        

    def colonize(self):
      self.exists=False