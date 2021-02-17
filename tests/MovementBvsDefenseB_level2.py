import random
import math
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level2strats.defense_beserker2 import DefenseBerserkerLevel2
from strategies.level2strats.movement_berserker2 import MovementBerserkerLevel2

for game_num in range(1,6):
    random.seed(game_num)
    first_few_die_rolls = [math.ceil(10*random.random()) for _ in range(7)]
    print('first few die rolls of game {}'.format(game_num))
    print('\t',first_few_die_rolls,'\n')

win_dict={0:[],1:[]}#3 being a draw
for n in range(20):
  print(n)
  random.seed(n+1)
  if n<10:
    new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
    player1_strats=DefenseBerserkerLevel2(1)
    player0_strats=MovementBerserkerLevel2(0)

    player0=Player(0,player0_strats,(2,0),game=new_game)
    player1=Player(1,player1_strats,(2,4),game=new_game)
    new_game.setup([player0,player1])
    winner = new_game.run_until_winner()
    if winner != 3:
      win_dict[winner].append(n)
  else:
    new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
    player0_strats=DefenseBerserkerLevel2(0)
    player1_strats=MovementBerserkerLevel2(1)

    player0=Player(0,player0_strats,(2,0),game=new_game)
    player1=Player(1,player1_strats,(2,4),game=new_game)
    new_game.setup([player0,player1])
    winner = new_game.run_until_winner()
    if winner != 3:
      win_dict[abs(winner-1)].append(n)
print(win_dict)
