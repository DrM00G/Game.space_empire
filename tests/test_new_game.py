import sys
sys.path.append('src')
from game import Game
from strategies.dumb_strategy import DumbStrategy
from player import Player


game=Game(board_size=[5,5],die_mode="random")
player0_strats=DumbStrategy(0)
player1_strats=DumbStrategy(1)

player0=Player(0,player0_strats,[2,0],game=game)
player1=Player(1,player1_strats,[2,4],game=game)
game.setup([player0,player1])
print(game.generate_state())