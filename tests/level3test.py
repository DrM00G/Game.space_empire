import random
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level3strats.numbers_berserker3 import NumbersBerserkerLevel3
from strategies.level3strats.custom_davidstrat3 import DavidStrategyLevel3
def run_half_matchup(strat0,strat1,win_dict,sample_size,phase):
  for n in range(int(sample_size/2)):
    random.seed(n+phase*(sample_size/2)+1)
    if (n+phase*(sample_size/2))%100==0:    
      print("turn: "+str(n+phase*(sample_size/2)))
    new_game=Game(board_size=[7,7],die_mode="random",sided_die=10,simple=True, level=3)
    player1_strats=strat1
    player0_strats=strat0

    player0=Player(0,player0_strats,(3,0),game=new_game)
    player1=Player(1,player1_strats,(3,6),game=new_game)
    new_game.setup([player0,player1])
    winner = new_game.run_until_winner()
    if phase==0 or winner==2:
      win_dict[winner].append(n)
    else:
      win_dict[abs(winner-1)].append(n)
  return win_dict

def run_matchup(stratA,stratB,sample_size):
  win_dict={0:[],1:[],2:[]}
  stratA.player_index=0
  stratB.player_index=1
  win_dict=run_half_matchup(stratA,stratB,win_dict,sample_size,0)
  stratA.player_index=1
  stratB.player_index=0
  win_dict=run_half_matchup(stratB,stratA,win_dict,sample_size,1)
  print("A: %"+str(100*len(win_dict[0])/sample_size)+"B: %"+str(100*len(win_dict[1])/sample_size)+"Draw:%"+str(100*len(win_dict[2])/sample_size))

David=DavidStrategyLevel3("David")
Beserk=NumbersBerserkerLevel3("Ooga")

run_matchup(David,Beserk,10)