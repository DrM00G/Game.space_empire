
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level2strats.numbers_berserker2 import NumbersBerserkerLevel2
from strategies.level2strats.custom_davidstrat2 import HoldbackBeserkerLevel2
from strategies.level2strats.custom_rileystrat2 import RileyStrategyLevel2
from strategies.level2strats.custom_elistrat2 import ElijahStrategyLevel2
from strategies.level2strats.custom_justinstrat2 import JustinStrategyLevel2

def run_half_matchup(strat0,strat1,win_dict,sample_size,phase):
  for n in range(int(sample_size/2)):
    if n%50==0:    
      print(n+phase*(sample_size/2))
    new_game=Game(board_size=[5,5],die_mode="random",sided_die=10,simple=True, level=2)
    player1_strats=strat1
    player0_strats=strat0

    player0=Player(0,player0_strats,(2,0),game=new_game)
    player1=Player(1,player1_strats,(2,4),game=new_game)
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
  win_dict=run_half_matchup(stratA,stratB,win_dict,50,0)
  stratA.player_index=1
  stratB.player_index=0
  win_dict=run_half_matchup(stratB,stratA,win_dict,50,1)
  print("A: %"+str(len(win_dict[0])/sample_size)+"B: %"+str(len(win_dict[1])/sample_size)+"Draw:%"+str(len(win_dict[2])/sample_size))

David=HoldbackBeserkerLevel2("David")
NumBeserker=NumbersBerserkerLevel2("Robot")
Riley=RileyStrategyLevel2("Riley")
Eli=ElijahStrategyLevel2("Eli")
Justin=JustinStrategyLevel2("Justin")
print("RileyvsDavid")
run_matchup(Riley,David,500)
print("RileyvsEli")
run_matchup(Riley,Eli,500)
print("RileyvsJustin")
run_matchup(Riley,Justin,500)
