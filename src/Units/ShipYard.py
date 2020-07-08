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