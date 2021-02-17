import random
import math
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level2strats.numbers_berserker2 import NumbersBerserkerLevel2
from strategies.level2strats.flanker2 import FlankerStrategyLevel2
from strategies.level2strats.custom_davidstrat2 import HoldbackBeserkerLevel2

new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
player1_strats=HoldbackBeserkerLevel2(1)
player0_strats=NumbersBerserkerLevel2(0)

player0=Player(0,player0_strats,(2,0),game=new_game)
player1=Player(1,player1_strats,(2,4),game=new_game)
new_game.setup([player0,player1])
winner = new_game.run_until_winner()
print(winner)


# win_dict={0:[],1:[]}#3 being a draw
# for n in range(1000):
#   # print(n)
#   # random.seed(n+1)
#   if n<500:
#     new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
#     player1_strats=HoldbackBeserkerLevel2(1)
#     player0_strats=NumbersBerserkerLevel2(0)

#     player0=Player(0,player0_strats,(2,0),game=new_game)
#     player1=Player(1,player1_strats,(2,4),game=new_game)
#     new_game.setup([player0,player1])
#     winner = new_game.run_until_winner()
#     if winner != 3:
#       win_dict[winner].append(n)
#   else:
#     new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
#     player0_strats=HoldbackBeserkerLevel2(0)
#     player1_strats=NumbersBerserkerLevel2(1)

#     player0=Player(0,player0_strats,(2,0),game=new_game)
#     player1=Player(1,player1_strats,(2,4),game=new_game)
#     new_game.setup([player0,player1])
#     winner = new_game.run_until_winner()
#     if winner != 3:
#       win_dict[abs(winner-1)].append(n)
# print(len(win_dict[1])/(len(win_dict[0])+1))



# win_dict={0:[],1:[]}#3 being a draw
# for n in range(1000):
#   print(n)
#   # random.seed(n+1)
#   if n<500:
#     new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
#     player1_strats=HoldbackBeserkerLevel2(1)
#     player0_strats=FlankerStrategyLevel2(0)

#     player0=Player(0,player0_strats,(2,0),game=new_game)
#     player1=Player(1,player1_strats,(2,4),game=new_game)
#     new_game.setup([player0,player1])
#     winner = new_game.run_until_winner()
#     if winner != 3:
#       win_dict[winner].append(n)
#   else:
#     new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
#     player0_strats=HoldbackBeserkerLevel2(0)
#     player1_strats=FlankerStrategyLevel2(1)

#     player0=Player(0,player0_strats,(2,0),game=new_game)
#     player1=Player(1,player1_strats,(2,4),game=new_game)
#     new_game.setup([player0,player1])
#     winner = new_game.run_until_winner()
#     if winner != 3:
#       win_dict[abs(winner-1)].append(n)
# print(len(win_dict[1])/(len(win_dict[0])+1))