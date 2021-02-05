from units.unit import Unit

class Shipyard(Unit):
    def __init__(self,player,unit_index,p_index,init_coords,turn_bought,tech):
        super().__init__(player,unit_index,p_index,init_coords,turn_bought)
        self.can_move=False
        self.attack = 3 + tech[0]
        self.defense = 0 + tech[1]
        self.tactics = 3
        self.movement = tech[2]
        self.spyd_tech = tech[3]
        self.armor = 1
        self.name = 'Shipyard'
        self.combat_ready = True
        self.occupy_colony(init_coords)

    def occupy_colony(self,coords):
        for unit in self.player.board.board_dict[coords]["units"]:
          if unit.name=="Colony":
            unit.assets.append(self)



        
1