class NumbersBerserkerLevel3:

    def __init__(self, player_index):
        self.player_index = player_index
        self.name = 'berserk'

    def decide_ship_movement(self, ship_index, game_state):
        ship_coords = game_state['players'][self.player_index]['units'][ship_index]['coords']
        their_home = game_state['players'][self.player_index-1]['home_coords']
        return(self.move_to_target(ship_coords,their_home))

    def decide_removal(self, player_state):
        return -1
        
    def decide_which_unit_to_attack(self, hidden_game_state_for_combat, combat_state, coords, attacker_index):
        combat_order = combat_state[coords]
        player_indices = [unit['player'] for unit in combat_order]

        opponent_index = 1 - self.player_index
        for combat_index, unit in enumerate(combat_order):
            if unit['player'] == opponent_index:
                return combat_index

    def move_to_target(self,current_pos,target):
      if current_pos[1]-target[1]!=0:
        if target[1]-current_pos[1]>0:
          return (0,1)
        else:
          return (0,-1)
      elif current_pos[0]-target[0]!=0:
        if target[0]-current_pos[0]>0:
          return (1,0)
        else:
          return (-1,0)
      else:
        return (0,0)

    def decide_purchases(self,game_state):
        return_dict={
           'units': [],
           'technology': []}
        my_home=game_state['players'][self.player_index]["home_coords"]
        home_colony_ship_capacity=len([shipyard for shipyard in game_state['players'][self.player_index]["units"] if shipyard["type"]=="Shipyard" and shipyard['coords']==my_home])
        current_cp = game_state['players'][self.player_index]['cp']
        while current_cp>=game_state['unit_data']['Scout']['cp_cost'] and home_colony_ship_capacity>=game_state['unit_data']['Scout']['hullsize']:
            current_cp-=game_state['unit_data']['Scout']['cp_cost']
            home_colony_ship_capacity -= game_state['unit_data']['Scout']['hullsize']
            return_dict['units'].append({'type': 'Scout', 'coords': game_state['players'][self.player_index]['home_coords']})
        return return_dict