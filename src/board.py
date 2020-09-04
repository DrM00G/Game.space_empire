class Board:
    def __init__(self):
      self.positions = [[[[],[]] for x in range(7)] for y in range(7)]


    def setup(self,planets,players):
      for planet in planets: 
        if planet.colony_status == True:
          self.positions[planet.coords[1]][planet.coords[0]][0].append(["Colony",planet.player_control,planet])
        else:
          self.positions[planet.coords[1]][planet.coords[0]][0].append(["Planet",planet.colony_status,planet])
      for player in players:
        for unit in player.units:
          self.positions[unit.coordinates[1]][unit.coordinates[0]][1].append([unit.name,player.player_num,unit])
#[player.player_num - 1]

    def update_position(self,player,unit,Move):
      # print(Move)
      # print("--------------------------------------")
      # print(str(Move)+" DONE DID IT "+str(unit.coordinates[0])+","+str(unit.coordinates[1])+" "+unit.name)
              
      # print(self.positions[unit.coordinates[1]][unit.coordinates[0]][1])
      index_pos = self.positions[unit.coordinates[1]][unit.coordinates[0]][1].index([unit.name,player.player_num,unit])

      moving_unit = self.positions[unit.coordinates[1]][unit.coordinates[0]][1].pop(index_pos)

      if Move == 0:#stay
        self.positions[unit.coordinates[1]][unit.coordinates[0]][1].append(moving_unit)
      elif Move == 1:#right
        self.positions[unit.coordinates[1]][unit.coordinates[0]+1][1].append(moving_unit)
      elif Move == 2:#left
        self.positions[unit.coordinates[1]][unit.coordinates[0]-1][1].append(moving_unit)
      elif Move == 3:#up
        self.positions[unit.coordinates[1]+1][unit.coordinates[0]][1].append(moving_unit)
      elif Move == 4:#down
        self.positions[unit.coordinates[1]-1][unit.coordinates[0]][1].append(moving_unit)
      
      # for y in self.positions:
      #   for x in y:
      #     for unit in x[1]:
      #       if unit == moving_unit:
      #         print(str(y.index(x))+","+str(self.positions.index(y)))
      # print("--------------------------------------")
     
    def add_unit_to_board(self,unit,player_num):
      self.positions[unit.coordinates[1]][unit.coordinates[0]][1].append([unit.name,player_num,unit])