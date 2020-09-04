import sys
sys.path.append('src')
from game import Game

game = Game(False, [1,2,3,4,5,6])
game.generate()
game.establish_shipyard()

game.movement_phase()
print("Turn 1: Testing unit positions")
for player in game.players:
  for unit in player.units:
    if unit.exist == True:
      assert unit.coordinates == (2,2),","+unit.name+": Wrong unit position Turn 1, unit at "+str(unit.coordinates)+" instead of 2,2"
print("Turn 1: Movement tests passed")
game.attack_phase(True)


game.economic_phase()



