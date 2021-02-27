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
        self.name = 'Colonyship'
        self.combat_ready = False
        

    def colonize(self):
      self.exists=False

    def state(self):
      return {"type": self.name,
            "unit_num":self.unit_index,
            "coords":self.coords,
            "technology":{"defense": self.defense,"attack": self.attack,"movement": self.movement},
            "hits_left":self.armor,
            'turn_created':self.turn_made,
            'exists':self.exists
            }