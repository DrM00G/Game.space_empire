import random

class CombatEngine:
    def __init__(self,die_mode,sided_die,board):
      self.board=board
      self.die_mode=die_mode
      self.sided_die=sided_die
      self.rolls=[]
      self.roll_die()

    def roll_die(self):
      if self.die_mode=="random":
        for n in range(self.die_mode):
          self.rolls.append(random.randint(1,self.sided_die))
      else:
        self.rolls=[n+1 in range(self.sided_die)]
        if self.die_mode=="decending":
          self.rolls=self.rolls.reverse()

    def locate_combat(self):
      combat_dict={}
      for coord in self.board:
        if len(self.board[coord]["units"])>1:
          player_count=[0,0]
          for unit in self.board[coord]["units"]:
            player_count[unit.player_index]+=1
          if player_count[0]!=0 and player_count[1]!=0:
            combat_dict[coord]={}
            combat_dict[coord]["units"]= [
            {"type": unit.name,
            "unit_num":unit.unit_index,
            "coords":unit.coords,
            "technology":{"defense": unit.defense,"attack": unit.attack,"movement": unit.movement},
            "hits_left":unit.armor,
            'turn_created':unit.turn_made
            }for unit in self.board[coord]["units"]]
            if player_count[0]>player_count[1]:
              combat_dict[coord]["upperhand"] = 0
            elif player_count[0]<player_count[1]:
              combat_dict[coord]["upperhand"] = 1
            else:
              combat_dict[coord]["upperhand"] = None

            return combat_dict


    def kill_bystanders(self,combat_state):
        for coord in combat_state:
          for unit in self.board[coord]["units"]:
            if unit.combat_ready != True:
              unit.destroy

    def complete_combat_phase(self):
        self.kill_bystanders(self.locate_combat())
        while len(self.locate_combat()):
          



