import random

class MovementEngine:
    def __init__(self, game):
        self.order = []
        self.game = game
        self.players = self.game.players
        self.board = self.game.board


    def move(self, phase, unit):
        if unit.exist == True:
            if phase == 1:  #works
                moves = int((unit.speed) / 4) + 1
            elif phase == 2:  #works
                moves = int((unit.speed) / 3) + 1
            else:  #works
                moves = int((unit.speed + 1) / 3)
            # unit.player.game.boolean_print("phase: "+str(phase)+" Speed: "+str(self.speed)+" Moves: "+str(moves))
            move_made = 0
            print(self.generate_movement_state(phase))
            for i in range(moves):
                if unit.player.dumb_status == False:

                    for n in range(2):
                        for m in range(2):
                            if unit.coordinates[
                                    0] == n * 6 and unit.coordinates[
                                        1] == m * 6:
                                Move = random.choice([0, 1 + n, 3 + m])
                                move_made = 1

                    if move_made == 0:
                        for n in range(2):
                            for m in range(2):
                                if unit.coordinates[n] == m * 6:
                                    Move = random.choice([
                                        0, 1 + m * (1 - n), 3 - n,
                                        4 - n * (1 - m)
                                    ])
                                    move_made = 1

                    if move_made == 0:
                        Move = random.randint(0, 4)

                    unit.player.Game.board.update_position(
                        unit.player, unit, Move)

                    if Move == 0:  #stay
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1])
                    elif Move == 1:  #right
                        unit.coordinates = (unit.coordinates[0] + 1,
                                            unit.coordinates[1])
                    elif Move == 2:  #left
                        unit.coordinates = (unit.coordinates[0] - 1,
                                            unit.coordinates[1])
                    elif Move == 3:  #up
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1] + 1)
                    elif Move == 4:  #down
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1] - 1)
                else:
                    if unit.player.player_type != "combat":
                        if unit.coordinates[1] != 0:
                            Move = 4
                        else:
                            Move = 0

                        unit.player.Game.board.update_position(
                            unit.player, self, Move)


                        if Move == 0:  #stay
                            unit.coordinates = (unit.coordinates[0],
                                                unit.coordinates[1])
                        elif Move == 4:  #down
                            unit.coordinates = (unit.coordinates[0],
                                                unit.coordinates[1] - 1)
                    else:
                        if unit.coordinates[1] > 2:
                            Move = 4
                        elif unit.coordinates[1] < 2:
                            Move = 3
                        else:
                            Move = 0


                    if Move == 0:  #stay
                        unit.player.Game.board.update_position(
                            unit.player, unit, Move)
                        unit.coordinates = (unit.coordinates[0],
                                            unit.coordinates[1])
                    elif Move == 3:  #up
                        if unit.coordinates[1] != 6:
                            unit.player.Game.board.update_position(
                                unit.player, unit, Move)
                            unit.coordinates = (unit.coordinates[0],
                                                unit.coordinates[1] + 1)
                    elif Move == 4:  #down
                        if unit.coordinates[1] != 0:
                            unit.player.Game.board.update_position(
                                unit.player, unit, Move)
                            unit.coordinates = (unit.coordinates[0],
                                                unit.coordinates[1] - 1)


        unit.player.game.boolean_print("Unit " + str(unit.unit_number) + " (" +
                                       unit.name + ") moves to " +
                                       str(unit.coordinates[0]) + "," +
                                       str(unit.coordinates[1]))

    def generate_movement_state(self,round):
      state_dict={"round": round}
      return state_dict
