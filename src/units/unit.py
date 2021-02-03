class Unit:
    def __init__(self,unit_index,p_index,init_coords,turn_bought):
      self.unit_index=unit_index
      self.player_index=p_index
      self.coords=init_coords
      self.turn_made=turn_bought
      self.exists = True
