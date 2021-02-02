class Planet:
    def __init__(self, coords, playerNum):
        self.coords = coords
        self.colony_status = False
        self.player_control = playerNum


    def destroy_colony(self):
        self.colony_status = False

