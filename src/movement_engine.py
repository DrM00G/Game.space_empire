import random

class MovementEngine:
    def __init__(self, game):
        self.order = []
        self.game = game
        self.players = self.game.players
        self.board = self.game.board


    def move(self, phase, unit,game_state):
        if unit.exist == True:
            if phase == 1:  #works
                moves = int((unit.speed) / 4) + 1
            elif phase == 2:  #works
                moves = int((unit.speed) / 3) + 1
            else:  #works
                moves = int((unit.speed + 1) / 3)

            for i in range(moves):



                    Move = unit.player.strategy.decide_ship_movement(unit,game_state)


                    unit.player.Game.board.update_position(
                        unit.player, unit, Move)

                    if Move == "Stay":  #stay
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1])
                    elif Move == "Right":  #right
                        unit.coordinates = (unit.coordinates[0] + 1,
                                            unit.coordinates[1])
                    elif Move == "Left":  #left
                        unit.coordinates = (unit.coordinates[0] - 1,
                                            unit.coordinates[1])
                    elif Move == "Up":  #up
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1] + 1)
                    elif Move == "Down":  #down
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1] - 1)
                


    def generate_movement_state(self,round):
      state_dict={"round": round}
      return state_dict
