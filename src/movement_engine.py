class MovementEngine:
    def __init__(self,board):
        self.board=board

    def move(self, phase, unit,game_state):
        if unit.exists and unit.can_move:
            if phase == 1:  #works
                moves = int((unit.movement) / 4) + 1
            elif phase == 2:  #works
                moves = int((unit.movement) / 3) + 1
            elif 3:  #works
                moves = int((unit.movement + 1) / 3)

            for i in range(moves):
                    print("check 1?")

                    
                    # print(game_state)
                    # print(unit.unit_index)
                    # print(unit.player_index)
                    Move = unit.player.strat.decide_ship_movement(unit.unit_index,game_state)
                    print("check 2?")

                    # print(str(unit.coords)+","+str(Move))
                    self.board.update_position(unit, Move)

                    
                    unit.coords = (unit.coords[0]+Move[0],
                                            unit.coords[1]+Move[1])
                    
                

