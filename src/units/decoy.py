from units.unit import Unit


class Decoy(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "F"
        self.strength = 0
        self.defense = 0 
        self.class_num = 0
        self.speed = 1 + tech[2]
        self.armor = 0
        self.name = 'Decoy'
        self.unit_number = unit_number+1
