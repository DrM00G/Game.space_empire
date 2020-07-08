from Units.Unit import Unit
class Battleship(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "A"
        self.strength = 5 + tech[0]
        self.defense = 2 + tech[1]
        self.class_num = 5
        self.speed = 1 + tech[2]
        self.armor = 3
        self.name = 'Battleship'
        self.unit_number = unit_number+1