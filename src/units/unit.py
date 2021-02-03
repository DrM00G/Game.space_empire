class Unit:
    def __init__(self,player,unit_index,p_index,init_coords,turn_bought):
      self.unit_index=unit_index
      self.player_index=p_index
      self.player=player
      self.coords=init_coords
      self.turn_made=turn_bought
      self.exists = True

    def destroy(self):
      self.exists=False
      self.player.board.remove_from_board(self)
