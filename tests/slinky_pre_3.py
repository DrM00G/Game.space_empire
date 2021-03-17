import sys
sys.path.append('src')

import math
import random
from game import Game
from player import Player
from strategies.level2strats.slinkystrats.Stationarystrat import StationaryStrategy
from strategies.level2strats.slinkystrats.Berserkerstrat import BerserkerStrategy



def run_individual_game(stratA, stratB, game_numb):
    # print("Game numb:"+str(game_numb))
    random.seed(game_numb+1)
    numb_collect = []
    for n in range(5):
        numb_collect.append(math.ceil(10*random.random()))

    stratA.player_index = 0
    stratB.player_index = 1

    new_game = Game(board_size=[7, 7], die_mode="random",
                    sided_die=10, simple=True, level=3, log=True, log_name="Slinky")

    player0 = Player(0, stratA, (3, 0), game=new_game)
    player1 = Player(1, stratB, (3, 6), game=new_game)
    new_game.setup([player0, player1])
    winner = new_game.run_until_winner()
    print(winner)
    print(numb_collect)
    return(winner)


Beserk = BerserkerStrategy(0)
Station = StationaryStrategy(1)

run_individual_game(Beserk, Station, 0)
