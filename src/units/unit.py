class Unit:
    def __init__(self,player,unit_index,p_index,init_coords,turn_bought):
      self.unit_index=unit_index
      self.player_index=p_index
      self.player=player
      self.coords=init_coords
      self.turn_made=turn_bought
      self.exists = True
      self.screaned=False

    def destroy(self):
      # print("Boing")
      self.exists=False
      self.player.board.remove_from_board(self)
      self.player.units.remove(self)

    def update_index(self):
      self.unit_index=self.player.units.index(self)

    