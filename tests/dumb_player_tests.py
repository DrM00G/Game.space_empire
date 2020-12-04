import sys
sys.path.append('src')
from game import Game

game = Game(False, [6,5,4,3,2,1],planet_amount=0)
game.generate()
game.establish_shipyard()

game_state = game.generate_state()
print(game_state)
player_0_scout_locations = [tuple(u['Coordinates']) for u in game_state['Players'][0]['Units'] if u['Name'] == 'Scout']
player_1_scout_locations = [tuple(u['Coordinates']) for u in game_state['Players'][1]['Units'] if u['Name'] == 'Scout']
assert set(player_0_scout_locations) == set([(2,0), (2,0), (2,0)]),"Coords are "+str(player_0_scout_locations)
assert set(player_1_scout_locations) == set([(2,4), (2,4), (2,4)]),"Coords are "+str(player_1_scout_locations)
print("Scount set up succesful")

game.movement_phase()
game_state = game.generate_state()
player_0_scout_locations = [tuple(u['Coordinates']) for u in game_state['Players'][0]['Units'] if u['Name'] == 'Scout']
player_1_scout_locations = [tuple(u['Coordinates']) for u in game_state['Players'][1]['Units'] if u['Name'] == 'Scout']
assert set(player_0_scout_locations) == set([(4,0), (4,0), (4,0)]),"Coords are "+str(player_0_scout_locations)
assert set(player_1_scout_locations) == set([(4,4), (4,4), (4,4)]),"Coords are "+str(player_1_scout_locations)
print("Turn 1 Movement Phase succesful")

game.economic_phase()

game_state = game.generate_state()
player_0_cp = game_state['Players'][0]['CP'] 
player_1_cp = game_state['Players'][1]['CP'] 
assert player_0_cp == 11,"Cp is "+str(player_0_cp)
assert player_1_cp == 11,"CP "+str(player_1_cp)
print("Turn 1 Economic Phase: succesful")
#Still working on getting it working