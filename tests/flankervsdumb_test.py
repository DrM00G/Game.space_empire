import random
import math
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level1strats.dumb_strat1 import LevelOneDumbStrategy

from strategies.level1strats.flanker_strat1 import FlankerStrategyLevel1


win_dict={0:0,1:0}
for n in range(1000):
  print(n)
  new_game=Game(board_size=[5,5],die_mode="random",sided_die=10)
  player0_strats=LevelOneDumbStrategy(0)
  player1_strats=FlankerStrategyLevel1(1)

  player0=Player(0,player0_strats,(2,0),game=new_game,simple_army=True)
  player1=Player(1,player1_strats,(2,4),game=new_game,simple_army=True)
  new_game.setup([player0,player1])
  win_dict[new_game.run_until_winner()]+=1
print(win_dict)