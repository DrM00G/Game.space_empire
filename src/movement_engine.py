class MovementEngine:
    def __init__(self,board):
        self.board=board

    def move(self, phase, unit,game_state):
        if unit.exist == True :
            if phase == 1:  #works
                moves = int((unit.movement) / 4) + 1
            elif phase == 2:  #works
                moves = int((unit.movement) / 3) + 1
            else:  #works
                moves = int((unit.movement + 1) / 3)

            for i in range(moves):


                    Move = unit.player.strategy.decide_ship_movement(unit.unit_index,game_state)


                    self.board.update_position(
                        unit.player, unit, Move)

                    
                    unit.coordinates = (unit.coordinates[0]+Move[0],
                                            unit.coordinates[1]+Move[1])
                    
                

