from units.unit import Unit

class Cruiser(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "C"
        self.strength = 4 + tech[0]
        self.defense = 1 + tech[1]
        self.class_num = 3
        self.speed = 1 + tech[2]
        self.armor = 2
        self.name = 'Cruiser'
        self.unit_number = unit_number+1