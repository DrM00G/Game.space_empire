
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

class Scout(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "E"
        self.strength = 3 + tech[0]
        self.defense = 0 + tech[1]
        self.class_num = 1
        self.speed = 2 + tech[2]
        self.armor = 1
        self.name = 'Scout'
        self.unit_number = unit_number+1

class Destroyer(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "D"
        self.strength = 4 + tech[0]
        self.defense = 0 + tech[1]
        self.class_num = 2
        self.speed = 1 + tech[2]
        self.armor = 1
        self.name = 'Destroyer'
        self.unit_number = unit_number+1

class ShipYard(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "C"
        self.strength = 3 + tech[0]
        self.defense = 0 + tech[1]
        self.class_num = 3
        self.speed = 1 + tech[2]
        self.armor = 1
        self.name = 'ShipYard'
        self.unit_number = unit_number+1
        self.technology = player.ship_yard_technology
        self.landed = False

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

class Battlecruiser(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "B"
        self.strength = 5 + tech[0]
        self.defense = 1 + tech[1]
        self.class_num = 4
        self.speed = 1 + tech[2]
        self.armor = 2
        self.name = 'Battlecruiser'
        self.unit_number = unit_number+1

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

class Dreadnaught(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "A"
        self.strength = 6 + tech[0]
        self.defense = 3 + tech[1]
        self.class_num = 5
        self.speed = 1 + tech[2]
        self.armor = 3
        self.name = 'Dreadnaught'
        self.unit_number = unit_number+1

class Base(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "A"
        self.strength = 7
        self.defense = 2
        self.class_num = 5
        self.speed = 0
        self.armor = 3
        self.name = 'Base'
        self.unit_number = unit_number+1
