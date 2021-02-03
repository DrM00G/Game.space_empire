class Board:
    def __init__(self,board_size):
      all_coords=[(x,y) for y in range(board_size[0]) for x in range(board_size[1])]
      self.board_dict={coord:{"units":[],"planet":None} for coord in all_coords}

    def update_position(self, unit, Move):
      self.board_dict[unit.coords]["units"].remove(unit)
      self.board_dict[(unit.coords[0]+Move[0],unit.coords[1]+Move[1])]["units"].append(unit)

    def add_to_board(self,unit):
      self.board_dict[unit.coords]["units"].append(unit)

    def remove_from_board(self,unit):
      self.board_dict[unit.coords]["units"].remove(unit)