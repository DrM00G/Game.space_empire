import sys
sys.path.append('src')
from strategies.level3strats.custom_colbystrat3 import ColbySiegeStrategyLevel3
from strategies.level3strats.custom_georgestrat3 import GeorgeStrat3
from strategies.level3strats.custom_elistrat3 import ElijahLevel3
from strategies.level3strats.custom_rileystrat3 import RileyStrategyLevel3
from strategies.level3strats.custom_davidstrat3 import DavidStrategyLevel3
from strategies.level3strats.numbers_berserker3 import NumbersBerserkerLevel3
from player import Player
from game import Game
import random
import math

# from strategies.level2strats.custom_justinstrat2 import JustinStrategyLevel2


def run_half_matchup(strat0, strat1, win_dict, sample_size, phase):
    for n in range(int(sample_size/2)):

        winner = run_individual_game(strat0, strat1, n+phase*(sample_size/2))

        if phase == 0 or winner == 2:
            win_dict[winner].append(n+phase*(sample_size/2))
        else:
            win_dict[abs(winner-1)].append(n+phase*(sample_size/2))
    return win_dict


def run_matchup(stratA, stratB, sample_size):
    win_dict = {0: [], 1: [], 2: []}

    win_dict = run_half_matchup(stratA, stratB, win_dict, sample_size, 0)

    win_dict = run_half_matchup(stratB, stratA, win_dict, sample_size, 1)
    print(win_dict[1])
    print("A: %"+str(100*len(win_dict[0])/sample_size)+"B: %"+str(100*len(
        win_dict[1])/sample_size)+"Draw:%"+str(100*len(win_dict[2])/sample_size))


def run_individual_game(stratA, stratB, game_numb):
    # print("Game numb:"+str(game_numb))
    print("Strat 0: "+stratA.name+" Game: "+str(game_numb))
    random.seed(game_numb+1)
    numb_collect = []
    for n in range(5):
      numb_collect.append(math.ceil(10*random.random()))
    
    stratA.player_index = 0
    stratB.player_index = 1
    

    new_game = Game(board_size=[7, 7], die_mode="random",
                    sided_die=10, simple=True, level=3, log=True)

    player0 = Player(0, stratA, (3, 0), game=new_game)
    player1 = Player(1, stratB, (3, 6), game=new_game)
    new_game.setup([player0, player1])
    winner = new_game.run_until_winner()
    print(winner)
    print(numb_collect)
    return(winner)


NumBeserker = NumbersBerserkerLevel3("Robot")
Colby = ColbySiegeStrategyLevel3("Colby")
George = GeorgeStrat3("George")
Riley = RileyStrategyLevel3("Riley")
Eli = ElijahLevel3("Eli")
David = DavidStrategyLevel3("David")
# Justin=JustinStrategyLevel2("Justin")

print("Level 3 Tournement")

# run_individual_game(David,George,82)
# run_individual_game(Colby,George,0)
print(run_individual_game(Eli, George, 58))


# print("ColbyvsGeorge")
# run_matchup(Colby,George,100)
# print("ColbyvsRiley")
# run_matchup(Colby,Riley,100)
# print("ColbyvsEli")
# run_matchup(Colby,Eli,100)
# print("ColbyvsDavid")
# run_matchup(Colby,David,100)
# print("ColbyvsJustin")
# # run_matchup(Colby,Justin,100)

# print("GeorgevsRiley")
# run_matchup(George,Riley,100)
# print("GeorgevsEli")
# run_matchup(George, Eli, 100)
# print("GeorgevsDavid")
# run_matchup(George,David,100)
# print("GeorgevsJustin")
# run_matchup(George,Justin,100)

# print("RileyvsDavid")
# run_matchup(Riley,David,100)
# print("RileyvsEli")
# run_matchup(Riley,Eli,100)
# print("RileyvsJustin")
# run_matchup(Riley,Justin,100)

# print("ElivsDavid")
# run_matchup(Eli,David,100)
# print("ElivsJustin")
# run_matchup(Eli,Justin,100)

# print("DavidvsJustin")
# run_matchup(David,Justin,100)

# print("BeserkvsColby")
# run_matchup(NumBeserker,Colby,100)
# print("BeserkvsGeorge")
# run_matchup(NumBeserker,George,100)
# print("BeserkvsRiley")
# run_matchup(NumBeserker,Riley,100)
# print("BeserkvsEli")
# run_matchup(NumBeserker,Eli,100)
# print("BeserkvsDavid")
# run_matchup(NumBeserker,David,100)
# print("BeserkvsJustin")
# run_matchup(NumBeserker,Justin,100)
