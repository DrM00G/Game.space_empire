import random
from board import Board



class Unit:
  def __init__(self,coordinates,player):
        self.coordinates = coordinates
        self.player = player
        self.exist = True

  def delete(self):
        self.exist = False

  def move(self,phase):
        if self.exist == True:
          if phase == 1:#works
            moves = int((self.speed)/4)+1
          elif  phase == 2:#works
            moves = int((self.speed)/3)+1
          else:#works
            moves = int((self.speed+1)/3)
          # self.player.game.boolean_print("phase: "+str(phase)+" Speed: "+str(self.speed)+" Moves: "+str(moves))
          move_made = 0
          for i in range(moves):
            # self.player.game.boolean_print(str(phase))
            if self.player.dumb_status == False:

              for n in range(2):
                for m in range(2):
                  if self.coordinates[0] == n*6 and self.coordinates[1] == m*6:
                    Move = random.choice([0,1+n, 3+m])
                    move_made = 1

              if move_made == 0:
                for n in range(2):
                  for m in range(2):
                    if self.coordinates[n] == m*6:
                      Move = random.choice([0, 1+m*(1-n),3-n, 4-n*(1-m)])
                      move_made = 1

              if move_made == 0:
                Move = random.randint(0, 4)
            

              self.player.Game.board.update_position(self.player,self,Move)


              # self.player.game.boolean_print("move?")
              if Move == 0:#stay
                    self.coordinates = (self.coordinates[0], self.coordinates[1])
              elif Move == 1:#right
                    self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
              elif Move == 2:#left
                    self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
              elif Move == 3:#up
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
              elif Move == 4:#down
                    self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
              # self.player.game.boolean_print("Moved")
            else:
              if self.player.player_type != "combat":
                if self.coordinates[1] != 0:
                  Move = 4
                else:
                  Move = 0

                self.player.Game.board.update_position(self.player,self,Move)
              
              # self.player.game.boolean_print("move?")

                if Move == 0:#stay
                      self.coordinates = (self.coordinates[0], self.coordinates[1])
                elif Move == 4:#down
                      self.coordinates = (self.coordinates[0], self.coordinates[1]-1)
              else:
                if self.coordinates[1] > 2:
                  Move = 4
                elif self.coordinates[1] < 2:
                  Move = 3
                else:
                  Move = 0

              
              # self.player.game.boolean_print("move?")

              if Move == 0:#stay
                      self.player.Game.board.update_position(self.player,self,Move)
                      self.coordinates = (self.coordinates[0], self.coordinates[1])
              elif Move == 3:#up
                    if self.coordinates[1] != 6:
                      self.player.Game.board.update_position(self.player,self,Move)
                      self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
              elif Move == 4:#down
                    if self.coordinates[1] != 0:
                      self.player.Game.board.update_position(self.player,self,Move)
                      self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)





              # self.player.game.boolean_print("Moved Down")
            
        self.player.game.boolean_print("Unit "+str(self.unit_number)+" ("+self.name+") moves to "+str(self.coordinates[0])+","+str(self.coordinates[1]))

              