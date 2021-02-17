class MovementBerserkerLevel2:
    # Sends all of its units directly towards the enemy home colony

    def __init__(self, player_num):
        self.player_num = player_num

    def decide_ship_movement(self, unit_index, hidden_game_state):
        myself = hidden_game_state['players'][self.player_num]
        opponent_index = 1 - self.player_num
        opponent = hidden_game_state['players'][opponent_index]

        unit = myself['units'][unit_index]
        x_unit, y_unit = unit['coords']
        x_opp, y_opp = opponent['home_coords']

        translations = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        best_translation = (0,0)
        smallest_distance_to_opponent = 999999999999
        for translation in translations:
            delta_x, delta_y = translation
            x = x_unit + delta_x
            y = x_unit + delta_y
            dist = abs(x - x_opp) + abs(y - y_opp)
            if dist < smallest_distance_to_opponent:
                best_translation = translation
                smallest_distance_to_opponent = dist

        return best_translation

    def decide_which_unit_to_attack(self, hidden_game_state_for_combat, combat_state, coords, attacker_index):
        combat_order = combat_state[coords]
        player_indices = [unit['player_num'] for unit in combat_order]

        opponent_index = 1 - self.player_num
        for combat_index, unit in enumerate(combat_order):
            if unit['player_num'] == opponent_index:
                return combat_index


    def decide_purchases(self,game_state):
      return_dic = {
            'units': [],
            'technology': [] 
        }
      current_cp = game_state['players'][self.player_num]['cp']
      new_movement= game_state['players'][self.player_num]['technology']['movement']
      if current_cp>=game_state['technology_data']['movement'][new_movement]:
          current_cp-=game_state['technology_data']['movement'][new_movement]
          new_movement= new_movement+1
          return_dic['technology'].append('movement')
      if current_cp>=game_state['unit_data']['Scout']['cp_cost']:
        current_cp-=game_state['unit_data']['Scout']['cp_cost']
        return_dic['units'].append({'type': 'Scout', 'coords': game_state['players'][self.player_num]['home_coords']})
      return return_dic