
import random
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level2strats.numbers_berserker2 import NumbersBerserkerLevel2
from strategies.level2strats.custom_davidstrat2 import HoldbackBeserkerLevel2
from strategies.level2strats.custom_rileystrat2 import RileyStrategyLevel2
from strategies.level2strats.custom_elistrat2 import ElijahStrategyLevel2
from strategies.level2strats.custom_justinstrat2 import JustinStrategyLevel2
from strategies.level2strats.custom_georgestrat2 import GeorgeStrategyLevel2
from strategies.level2strats.custom_colbystrat2 import ColbyStrategyLevel2

def run_half_matchup(strat0,strat1,win_dict,sample_size,phase):
  for n in range(int(sample_size/2)):
    random.seed(n+phase*(sample_size/2)+1)
    if (n+phase*(sample_size/2))%100==0:    
      print("turn: "+str(n+phase*(sample_size/2)))
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
  win_dict=run_half_matchup(stratA,stratB,win_dict,sample_size,0)
  stratA.player_index=1
  stratB.player_index=0
  win_dict=run_half_matchup(stratB,stratA,win_dict,sample_size,1)
  print("A: %"+str(100*len(win_dict[0])/sample_size)+"B: %"+str(100*len(win_dict[1])/sample_size)+"Draw:%"+str(100*len(win_dict[2])/sample_size))

NumBeserker=NumbersBerserkerLevel2("Robot")
Colby=ColbyStrategyLevel2("Colby")
George=GeorgeStrategyLevel2("George")
Riley=RileyStrategyLevel2("Riley")
Eli=ElijahStrategyLevel2("Eli")
David=HoldbackBeserkerLevel2("David")
Justin=JustinStrategyLevel2("Justin")

# print("ColbyvsGeorge")
# run_matchup(Colby,George,500)
# print("ColbyvsRiley")
# run_matchup(Colby,Riley,500)
# print("ColbyvsEli")
# run_matchup(Colby,Eli,500)
# print("ColbyvsDavid")
# run_matchup(Colby,David,500)
# print("ColbyvsJustin")
# run_matchup(Colby,Justin,500)

# print("GeorgevsRiley")
# run_matchup(George,Riley,500)
# print("GeorgevsEli")
# run_matchup(George,Eli,500)
# print("GeorgevsDavid")
# run_matchup(George,David,500)
# print("GeorgevsJustin")
# run_matchup(George,Justin,500)

# print("RileyvsDavid")
# run_matchup(Riley,David,500)
# print("RileyvsEli")
# run_matchup(Riley,Eli,500)
# print("RileyvsJustin")
# run_matchup(Riley,Justin,500)

# print("ElivsDavid")
# run_matchup(Eli,David,500)
# print("ElivsJustin")
# run_matchup(Eli,Justin,500)

# print("DavidvsJustin")
# run_matchup(David,Justin,500)

# print("BeserkvsColby")
# run_matchup(NumBeserker,Colby,500)
print("BeserkvsGeorge")
run_matchup(NumBeserker,George,500)
# print("BeserkvsRiley")
# run_matchup(NumBeserker,Riley,500)
# print("BeserkvsEli")
# run_matchup(NumBeserker,Eli,500)
# print("BeserkvsDavid")
# run_matchup(NumBeserker,David,500)
# print("BeserkvsJustin")
# run_matchup(NumBeserker,Justin,500)
