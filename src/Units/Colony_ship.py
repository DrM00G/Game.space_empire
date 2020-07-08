from Units.Unit import Unit
class Colony_ship(Unit):
    def __init__(self, coords, player,unit_number,tech):#0 is att, 1 is def, 2 is spd, not sure how to do it differantly while keeping the army set up code clean
        super().__init__(coords, player)
        self.class_type = "F"
        self.strength = 0
        self.defense = 0 
        self.class_num = 0
        self.speed = 1
        self.armor = 1
        self.name = 'Colony ship'
        self.unit_number = unit_number+1
