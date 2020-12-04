import sys
sys.path.append('src')
from game import Game

game = Game(False, [6,5,4,3,2,1],planet_amount=0)
game.generate()
game.establish_shipyard()

game_state = game.generate_state()
player_0_scout_locations = [tuple(u.coordinates) for u in game_state.players[0].units if u.name == 'Scout']
player_1_scout_locations = [tuple(u.coordinates) for u in game_state.players[1].units if u.name == 'Scout']
assert set(player_0_scout_locations) == set([(2,0), (2,0), (2,0)]),"Coords are "+str(player_0_scout_locations)
assert set(player_1_scout_locations) == set([(2,4), (2,4), (2,4)]),"Coords are "+str(player_1_scout_locations)
print("Scount set up succesful")

game.movement_phase()
game_state = game.generate_state()
player_0_scout_locations = [tuple(u.coordinates) for u in game_state.players[0].units if u.name == 'Scout']
player_1_scout_locations = [tuple(u.coordinates) for u in game_state.players[1].units if u.name == 'Scout']
assert set(player_0_scout_locations) == set([(4,0), (4,0), (4,0)]),"Coords are "+str(player_0_scout_locations)
assert set(player_1_scout_locations) == set([(4,4), (4,4), (4,4)]),"Coords are "+str(player_1_scout_locations)
print("Turn 1 Movement Phase succesful")
#Still working on getting it working