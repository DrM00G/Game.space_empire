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
