class NumbersBerserkerLevel2:

    def __init__(self, player_num):
        self.player_num = player_num
        self.name = 'berserk'

    def decide_ship_movement(self, ship_index, game_state):
        ship_coords = game_state['players'][self.player_num]['units'][ship_index]['coords']
        route = self.fastest_route(ship_coords, game_state['players'][self.player_num-1]['home_coords'])
        if len(route) > 0:
            return tuple(route[0])
        else:
            return (0,0)

    def decide_removals(self, player_state):
        return -1
        
    def decide_which_unit_to_attack(self, hidden_game_state, combat_state, location, attacker_index):
        # print(combat_state)
      for ship in combat_state[location]:
        if ship['player_num']!=self.player_num:
          return combat_state[location].index(ship)

    def directional_input(self, current, goal):
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1],[0,0]]
        distances = []
        for i in range(len(directions)):
            new_loc = [current[0] + directions[i][0], current[1] + directions[i][1]]
            dist = self.distance(new_loc, goal)
            distances.append(dist)
        closest = min(distances)
        index = distances.index(closest)
        return directions[index]

    def distance(self, current, goal):
        return ((current[0] - goal[0])**2 + (current[1] - goal[1])**2)**(0.5)

    def fastest_route(self, current, goal):
        route = []
        while(tuple(current) != goal):
            # print("check 1.02")
            direc = self.directional_input(current, goal)
            # print("check 1.03")
            route.append(direc)
            current  = [current[0] + direc[0], current[1] + direc[1]]
        return route

    def decide_purchases(self,game_state):
        return_dict={
           'units': [],
           'technology': []}
        current_cp = game_state['players'][self.player_num]['cp']
        while current_cp>=game_state['unit_data']['Scout']['cp_cost']:
          current_cp-=game_state['unit_data']['Scout']['cp_cost']
          return_dict['units'].append({'type': 'Scout', 'coords': game_state['players'][self.player_num]['home_coords']})
        return return_dict