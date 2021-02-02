from units.unit import Unit

class Colony(Unit):
    def __init__(self, coords, player,unit_number):
        super().__init__(coords, player)
        self.defense = 1
        self.class_num = 3
        self.speed = 0
        self.armor = 2
        self.name = 'Cruiser'
        self.unit_number = unit_number+1
        self.ship_yards = 0

