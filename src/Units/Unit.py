import random



class Unit:
  def __init__(self,coordinates,player):
        self.coordinates = coordinates
        self.player = player
        self.exist = True

  def delete(self):
        self.exist = False

  def move(self):
        if self.exist == True:
          move_made = 0
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
