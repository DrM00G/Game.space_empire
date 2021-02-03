import random
from board import Board




class Unit:
  def __init__(self,coordinates,player):
        self.coordinates = coordinates
        self.player = player
        self.exist = True

  def delete(self):
        self.exist = False


