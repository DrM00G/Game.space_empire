import sys
sys.path.append('src')
from game import Game

game = Game(False, [6,5,4,3,2,1],planet_amount=0)
game.generate()
game.establish_shipyard()

game.movement_phase()

game.attack_phase(True)