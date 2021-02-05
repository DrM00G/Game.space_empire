class LevelOneBerserkerStrategy:

    def __init__(self, player_num):
        self.player_num = player_num
        self.name = 'berserk'

    def decide_ship_movement(self, ship_index, game_state):
        print("check 1.1")
        ship_coords = game_state['players'][self.player_num]['units'][ship_index]['coords']
        print("check 1.2")
        route = self.fastest_route(ship_coords, game_state['players'][self.player_num-1]['home_coords'])
        print("check 1.3")
        if len(route) > 0:
            return tuple(route[0])
        else:
            return (0,0)

    def decide_removals(self, player_state):
        return -1
        
    def decide_which_unit_to_attack(self, combat_state, location, attacker_index):
        print(combat_state)
        for unit in combat_state[tuple(location)]:
            if unit['player'] != combat_state[tuple(location)][attacker_index]['player']:
                return combat_state[tuple(location)].index(unit)

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
        print("check 1.01")
        while(tuple(current) != goal):
            # print("check 1.02")
            direc = self.directional_input(current, goal)
            # print("check 1.03")
            route.append(direc)
            print(str(current)+","+str(goal))
            current  = [current[0] + direc[0], current[1] + direc[1]]
        print("check 1.05")
        return route