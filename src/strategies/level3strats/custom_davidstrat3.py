class DavidStrategyLevel3:

    def __init__(self, player_index):
        self.player_index = player_index
      
    def decide_ship_movement(self, ship_index, game_state):
        ship_coords = game_state['players'][self.player_index]['units'][ship_index]['coords']
        my_home=game_state['players'][self.player_index]["home_coords"]
        their_home = game_state['players'][self.player_index-1]['home_coords']
        
        if ship_coords == my_home:
          if (game_state["turn"]+2)%12==0 and ship_index%2==1:
            target=their_home
          elif (game_state["turn"]+2)%6==0 and ship_index%2==0:
            target=(my_home[0]+3,my_home[1])
          else:
            return (0,0)  
        else:
          if ship_index%2==0:
            if tuple(ship_coords)==(my_home[0]+1,my_home[1]) or tuple(ship_coords)==(my_home[0]+2,my_home[1]):
              target=(my_home[0]+3,my_home[1])
            else:
              target=their_home
          else:
            target=their_home

        if ship_index>7:
          return(self.move_to_target(ship_coords,target))
        else:
          return(0,0)



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

    def decide_removals(self, player_state):
        return -1
        
    def decide_which_unit_to_attack(self, hidden_game_state_for_combat, combat_state, coords, attacker_index):
        combat_order = combat_state[coords]

        opponent_index = 1 - self.player_index
        for combat_index, unit in enumerate(combat_order):
            if unit['player'] == opponent_index:
                return combat_index





    def decide_purchases(self,game_state):
        return_dict={
           'units': [],
           'technology': []}

        current_cp = game_state['players'][self.player_index]['cp']
        new_defense= game_state['players'][self.player_index]['technology']['defense']
        if game_state["turn"]<=2:
          if current_cp>=game_state['technology_data']['defense'][new_defense]:
            return_dict['technology'].append("defense")
        else:
          while current_cp>=game_state['unit_data']['Scout']['cp_cost']:
            current_cp-=game_state['unit_data']['Scout']['cp_cost']
            return_dict['units'].append({'type': 'Scout', 'coords': game_state['players'][self.player_index]['home_coords']})
        return return_dict