import sys
sys.path.append('src')
from game import Game
from strategies.combat_strategy import CombatStrategy
from stratagies_foriegn.george_combat import CombatStrategy_G

from player import Player

print('ASCENDING TESTS')

print('TURN 1 Economic')

new_game=Game(board_size=[5,5],die_mode="ascending",sided_die=6)
player0_strats=CombatStrategy_G(0)
player1_strats=CombatStrategy_G(1)

player0=Player(0,player0_strats,(2,0),game=new_game,simple_army=False)
player1=Player(1,player1_strats,(2,4),game=new_game,simple_army=False)
new_game.setup([player0,player1])


new_game.movement_phase()
new_game.combat_phase()
new_game.economic_phase()

location = (2,2)

new_or_non_moveable = [(2,0), (2,4)]

p1_scouts = []

def return_scouts(game_state, player_index):
    return [unit for unit in game_state['players'][player_index]['units'] if unit['type'] == 'Scout' and unit['exists']]
def return_destroyers(game_state, player_index):
    return [unit for unit in game_state['players'][player_index]['units'] if unit['type'] == 'Destroyer' and unit['exists']]
def return_ship_size_tech(game_state, player_index):
    return game_state['players'][player_index]['tech']['shipsize']
def return_cp(game_state, player_index):
    # print(game_state['players'][player_index]['cp'])
    return game_state['players'][player_index]['cp']

def check_unit_coords(units, coords):
    for unit in units:
      assert unit['coords'] == coords, str(unit['coords'])+","+str(coords)

assert return_cp(new_game.generate_state(), 0) == 7, return_cp(new_game.generate_state(), 0)
assert return_cp(new_game.generate_state(), 1) == 1, return_cp(new_game.generate_state(), 1)
print('Passed')

print('TURN 2 Movement')
new_game.movement_phase()
check_unit_coords(return_scouts(new_game.generate_state(), 0), (2,2))
assert len(return_scouts(new_game.generate_state(), 0)) == 3
check_unit_coords(return_destroyers(new_game.generate_state(), 0), (2,2))
assert len(return_destroyers(new_game.generate_state(), 0)) == 0
check_unit_coords(return_destroyers(new_game.generate_state(), 1), (2,2))
assert len(return_destroyers(new_game.generate_state(), 1)) == 1

print('Passed')

print('TURN 2 Combat')
new_game.combat_phase()
check_unit_coords(return_scouts(new_game.generate_state(), 0), (2,2))
assert len(return_scouts(new_game.generate_state(), 0)) == 1, return_scouts(new_game.generate_state(), 0)
check_unit_coords(return_destroyers(new_game.generate_state(), 0), (2,2))
assert len(return_destroyers(new_game.generate_state(), 0)) == 0
check_unit_coords(return_destroyers(new_game.generate_state(), 1), (2,2))
assert len(return_destroyers(new_game.generate_state(), 1)) == 0

print('Passed')


print('DESCENDING TESTS')
new_game=Game(board_size=[5,5],die_mode="decending",sided_die=6)
player0_strats=CombatStrategy(0)
player1_strats=CombatStrategy(1)

player0=Player(0,player0_strats,(2,0),game=new_game,simple_army=False)
player1=Player(1,player1_strats,(2,4),game=new_game,simple_army=False)
new_game.setup([player0,player1])

new_game.movement_phase()
new_game.combat_phase()
new_game.economic_phase()


print('TURN 1 Economic')

assert return_cp(new_game.generate_state(), 0) == 1
assert return_cp(new_game.generate_state(), 1) == 7
print('Passed')

print('TURN 2 Movement')
new_game.movement_phase()
check_unit_coords(return_scouts(new_game.generate_state(), 1), (2,2))
assert len(return_scouts(new_game.generate_state(), 1)) == 3
check_unit_coords(return_destroyers(new_game.generate_state(), 1), (2,2))
assert len(return_destroyers(new_game.generate_state(), 1)) == 0
check_unit_coords(return_destroyers(new_game.generate_state(), 0), (2,2))
assert len(return_destroyers(new_game.generate_state(), 0)) == 1

print('Passed')

print('TURN 2 Combat')
new_game.combat_phase()
check_unit_coords(return_scouts(new_game.generate_state(), 1), (2,2))
assert len(return_scouts(new_game.generate_state(), 1)) == 3
check_unit_coords(return_destroyers(new_game.generate_state(), 1), (2,2))
assert len(return_destroyers(new_game.generate_state(), 1)) == 0
check_unit_coords(return_destroyers(new_game.generate_state(), 0), (2,2))
assert len(return_destroyers(new_game.generate_state(), 0)) == 0

print('Passed')