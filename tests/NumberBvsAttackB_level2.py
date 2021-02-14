import random
import math
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level2strats.numbers_berserker2 import NumbersBerserkerLevel2
from strategies.level2strats.attack_berserker2 import AttackBerserkerLevel2

for game_num in range(1,6):
    random.seed(game_num)
    first_few_die_rolls = [math.ceil(10*random.random()) for _ in range(7)]
    print('first few die rolls of game {}'.format(game_num))
    print('\t',first_few_die_rolls,'\n')

# random.seed(4)
# new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True)
# player1_strats=LevelOneBerserkerStrategy(1)
# player0_strats=FlankerStrategyLevel1(0)

# player0=Player(0,player0_strats,(2,0),game=new_game)
# player1=Player(1,player1_strats,(2,4),game=new_game)
# new_game.setup([player0,player1])
# print(new_game.run_until_winner())

win_dict={0:[],1:[]}
for n in range(20):
  print(n)
  random.seed(n+1)
  if n<10:
    new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
    player1_strats=AttackBerserkerLevel2(1)
    player0_strats=NumbersBerserkerLevel2(0)

    player0=Player(0,player0_strats,(2,0),game=new_game)
    player1=Player(1,player1_strats,(2,4),game=new_game)
    new_game.setup([player0,player1])
    win_dict[new_game.run_until_winner()].append(n)
  else:
    new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
    player0_strats=AttackBerserkerLevel2(0)
    player1_strats=NumbersBerserkerLevel2(1)

    player0=Player(0,player0_strats,(2,0),game=new_game)
    player1=Player(1,player1_strats,(2,4),game=new_game)
    new_game.setup([player0,player1])
    win_dict[abs(new_game.run_until_winner()-1)].append(n)
print(win_dict)
