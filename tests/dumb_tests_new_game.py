import sys
sys.path.append('src')
from game import Game
from strategies.dumb_strategy import DumbStrategy
from player import Player

scout_coords = [(4,0), (4,4)]
non_scout_coords = [(2,0), (2,4)]
player_scouts = [3,5,8,10,12]

new_game=Game(board_size=[5,5],die_mode="decending",sided_die=6)
player0_strats=DumbStrategy(0)
player1_strats=DumbStrategy(1)

player0=Player(0,player0_strats,(2,0),game=new_game,simple_army=False)
player1=Player(1,player1_strats,(2,4),game=new_game,simple_army=False)
new_game.setup([player0,player1])


def check_player(player_index, scout_count, turn):
    state = new_game.generate_state()
    scouts = [unit['type'] for unit in state['players'][player_index]['units'] if unit['type'] == 'Scout']
    assert len(scouts) == scout_count
    for unit in state['players'][player_index]['units']:
        if unit['type'] == 'Scout':
            if unit['turn_created'] == turn:
                assert unit['coords'] == non_scout_coords[player_index]
            else:
                assert unit['coords'] == scout_coords[player_index]
        # else:
        #     assert unit['coords'] == non_scout_coords[player_index]
    print('Passed')

for i in range(4):
    print('===================================')
    new_game.turn_numb += 1
    new_game.movement_phase()
    print('Testing',i+1, 'Turn Movement Scouts')
    check_player(0, player_scouts[i], i+1)
    check_player(1, player_scouts[i], i+1)
    print('Testing',i+1, 'Turn Combat Phase')
    new_game.combat_phase()
    print('passed')
    new_game.economic_phase()
    print('Testing',i+1, 'Turn Economic Phase')
    check_player(0, player_scouts[i + 1], i+1)
    check_player(1, player_scouts[i + 1], i+1)
    print('===================================')
    # print(new_game.game_state())
