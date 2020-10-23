class Planet:
    def __init__(self, coords, colony_status, playerNum):
        self.coords = coords
        self.colony_status = colony_status
        self.player_control = playerNum
        self.health = 3
        self.ship_yards = 0
        self.base_status = 0

    def destroy_colony(self):
        self.colony_status = False
        self.player_control = 0
        self.health = 3
        self.base_status = 0
        self.ship_yards = 0
