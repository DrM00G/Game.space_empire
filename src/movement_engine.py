class MovementEngine:
    def __init__(self,board):
        self.board=board

    def move(self, phase, unit,game_state):
        if unit.exists and unit.can_move:
            if phase == 1:  #works
                moves = [1,1,1,2,2,2][unit.movement-1]
            elif phase == 2:  #works
                moves = [1,2,2,2,2,3][unit.movement-1]
            elif 3:  #works
                moves = [1,2,2,2,3,3][unit.movement-1]



            for i in range(moves):

                    
                    # print(game_state)
                    # print(unit.unit_index)
                    # print(unit.player_index)
                    Move = unit.player.strat.decide_ship_movement(unit.unit_index,game_state)
                    # print(str(unit.coords)+","+str(Move))
                    self.board.update_position(unit, Move)
          
                    unit.player.game.logger.info(str(unit.name)+str(unit.unit_index)+": "+str(unit.coords)+"-->"+str((unit.coords[0]+Move[0],
                                            unit.coords[1]+Move[1])))

                    
                    unit.coords = (unit.coords[0]+Move[0],
                                            unit.coords[1]+Move[1])
                    
                

