class Board:
    def __init__(self,board_size):
      self.board_size = board_size
      self.positions = [[[[],[]] for x in range(board_size[0])] for y in range(board_size[1])]


    def setup(self,planets,players):
      for planet in planets: 
        if planet.colony_status == True:
          self.positions[planet.coords[1]][planet.coords[0]][0].append(["Colony",planet.player_control,planet])
        else:
          self.positions[planet.coords[1]][planet.coords[0]][0].append(["Planet",planet.colony_status,planet])
      for player in players:
        for unit in player.units:
          self.positions[unit.coordinates[1]][unit.coordinates[0]][1].append([unit.name,player.player_num,unit])

    def update_position(self,player,unit,Move):

      index_pos = self.positions[unit.coordinates[1]][unit.coordinates[0]][1].index([unit.name,player.player_num,unit])

      moving_unit = self.positions[unit.coordinates[1]][unit.coordinates[0]][1].pop(index_pos)

      if Move == "Stay":#stay
        self.positions[unit.coordinates[1]][unit.coordinates[0]][1].append(moving_unit)
      elif Move == "Right":#right
        self.positions[unit.coordinates[1]][unit.coordinates[0]+1][1].append(moving_unit)
      elif Move == "Left":#left
        self.positions[unit.coordinates[1]][unit.coordinates[0]-1][1].append(moving_unit)
      elif Move == "Up":#up
        self.positions[unit.coordinates[1]+1][unit.coordinates[0]][1].append(moving_unit)
      elif Move == "Down":#down
        self.positions[unit.coordinates[1]-1][unit.coordinates[0]][1].append(moving_unit)
      

    def add_unit_to_board(self,unit,player_num):
      self.positions[unit.coordinates[1]][unit.coordinates[0]][1].append([unit.name,player_num,unit])
