import sys
sys.path.append('src')
from game import Game

game = Game(False, [6,5,4,3,2,1],planet_amount=0)
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
print("Turn 1: Testing unit survived")
existing_units = []
for player in game.players:
  for unit in player.units:
    if unit.exist == True:
      existing_units.append([unit.player.player_num,unit.name])
assert existing_units == [[1,'Scout'],[1,'Scout'],[1,'Scout']],"Wrong surviving units, is "+str(existing_units)+" but should be [[1,'Scout'],[1,'Scout'],[1,'Scout']]"
print("Turn 1: Combat tests passed")

#Combat is messed up

game.economic_phase()
print("Turn 1: Testing Cp levels")
nessisary_cp = [7,1]
for player in game.players:
      assert player.playerCP == nessisary_cp[player.player_num-1],"Wrong cp levels, Player "+str(player.player_num)+" should be "+str(nessisary_cp[player.player_num-1])+" not "+str(player.playerCP)+"."
print("Turn 1: Economic tests passed")

#Turn 2

game.movement_phase()
print("Turn 2: Testing unit positions")
for player in game.players:
  for unit in player.units:
    if unit.exist == True:
      assert unit.coordinates == (2,2),","+unit.name+": Wrong unit position Turn 2, unit at "+str(unit.coordinates)+" instead of 2,2"
print("Turn 2: Movement tests passed")

game.attack_phase(True)
print("Turn 2: Testing unit survived")
existing_units = []
for player in game.players:
  for unit in player.units:
    if unit.exist == True:
      existing_units.append([unit.player.player_num,unit.name])
assert existing_units == [[1,'Scout']],"Wrong surviving units, is "+str(existing_units)+" but should be [[1,'Scout']]"
print("Turn 2: Combat tests passed")



game2 = Game(False, [6,5,4,3,2,1])
game2.generate()
game2.establish_shipyard()

game2.movement_phase()
print("Turn 1: Testing unit positions")
for player in game2.players:
  for unit in player.units:
    if unit.exist == True:
      assert unit.coordinates == (2,2),","+unit.name+": Wrong unit position Turn 1, unit at "+str(unit.coordinates)+" instead of 2,2"
print("Turn 1: Movement tests passed")

game2.attack_phase(True)
print("Turn 1: Testing unit survived")
existing_units = []
for player in game2.players:
  for unit in player.units:
    if unit.exist == True:
      existing_units.append([unit.player.player_num,unit.name])
assert existing_units == [[2,'Scout'],[2,'Scout'],[2,'Scout']],"Wrong surviving units, is "+str(existing_units)+" but should be [[2,'Scout'],[2,'Scout'],[2,'Scout']]"
print("Turn 1: Combat tests passed")

#Combat is messed up

game2.economic_phase()
print("Turn 1: Testing Cp levels")
nessisary_cp = [1,7]
for player in game2.players:
      assert player.playerCP == nessisary_cp[player.player_num-1],"Wrong cp levels, Player "+str(player.player_num)+" should be "+str(nessisary_cp[player.player_num-1])+" not "+str(player.playerCP)+"."
print("Turn 1: Economic tests passed")

#Turn 2

game2.movement_phase()
print("Turn 2: Testing unit positions")
for player in game2.players:
  for unit in player.units:
    if unit.exist == True:
      assert unit.coordinates == (2,2),","+unit.name+": Wrong unit position Turn 2, unit at "+str(unit.coordinates)+" instead of 2,2"
print("Turn 2: Movement tests passed")

game2.attack_phase(True)
print("Turn 2: Testing unit survived")
existing_units = []
for player in game.players:
  for unit in player.units:
    if unit.exist == True:
      existing_units.append([unit.player.player_num,unit.name])
assert existing_units == [[2,'Scout'],[2,'Scout'],[2,'Scout']],"Wrong surviving units, is "+str(existing_units)+" but should be [[1,'Scout']]"
print("Turn 2: Combat tests passed")

