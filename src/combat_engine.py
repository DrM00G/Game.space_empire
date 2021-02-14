import random

class CombatEngine:
    def __init__(self,die_mode,sided_die,board,game):
      self.board=board
      self.die_mode=die_mode
      self.sided_die=sided_die
      self.rolls=[]
      self.roll_die()
      self.game=game

    def roll_die(self):
      if self.die_mode=="random":
        for n in range(self.sided_die):
          self.rolls.append(random.randint(1,self.sided_die))
      else:
        self.rolls=[n+1 for n in range(self.sided_die)]
        if self.die_mode=="decending":
          self.rolls=self.rolls[::-1]

    def locate_combat(self):
      combat_dict={}
      for coord in self.board.board_dict:
        if len(self.board.board_dict[coord]["units"])>1:
          player_count=[0,0]
          for unit in self.board.board_dict[coord]["units"]:
            player_count[unit.player_index]+=1
          if player_count[0]!=0 and player_count[1]!=0:
            combat_dict[coord]={}
            combat_dict[coord]= [
            {"type": unit.name,"player_index":unit.player_index,
            "unit_num":unit.unit_index,
            "coords":unit.coords,
            "technology":{"defense": unit.defense,"attack": unit.attack,"movement": unit.movement},
            "hits_left":unit.armor,
            'turn_created':unit.turn_made
            }for unit in self.board.board_dict[coord]["units"] if unit.screaned==False]
            # if player_count[0]>player_count[1]:
            #   combat_dict[coord]["upperhand"] = 0
            # elif player_count[0]<player_count[1]:
            #   combat_dict[coord]["upperhand"] = 1
            # else:
            #   combat_dict[coord]["upperhand"] = None

      return combat_dict


    def kill_bystanders(self,combat_state):
        for coord in combat_state:
          # print(self.board.board_dict[coord]["units"])
          # print([str(unit.name)+","+str(unit.unit_index) for unit in self.board.board_dict[coord]["units"]])
          units=[unit for unit in self.board.board_dict[coord]["units"]]
          for unit in units:
            # print(unit.name)
            if unit.combat_ready != True:
              
              unit.destroy()

    def combat_order(self,coord):
        seperations=[[]for n in range(6)]
        for player in range(2):
          for unit in self.board.board_dict[coord]["units"]:
            if unit.player_index == player:
              if unit.screaned == False:
                seperations[unit.tactics].append(unit)
        order=[]
        seperations=seperations[::-1]
        for i in range(6):
          for unit in seperations[i]:
            order.append(unit)
        # print([unit.name for unit in order])
        return order

    def complete_combat_phase(self):
        self.kill_bystanders(self.locate_combat())
        while len(self.locate_combat())>0 and self.game.winner==None:
          combat_coord=[key for key in self.locate_combat()][0]
          #SCREAN
          order = self.combat_order(combat_coord)
          for unit in order:
            if unit.exists and combat_coord in [key for key in self.locate_combat()] and self.game.winner==None and unit.name!="Colony":
              target=self.locate_combat()[combat_coord][unit.player.strat.decide_which_unit_to_attack(self.locate_combat(),self.locate_combat(), combat_coord,unit.unit_index)]
              for vs_unit in order:
                if vs_unit.unit_index==target["unit_num"] and vs_unit.player_index!=unit.player_index:
                  enemy=vs_unit

              self.do_combat(unit,enemy)

    def do_combat(self,attacker,target):
        if len(self.rolls) == 0:
          self.roll_die()
        roll=self.rolls[0]
        self.rolls.remove(roll)
        attack=attacker.attack-target.defense
        # print(str(roll)+"VS"+str(attack))
        self.game.logger.info(str(attacker.name)+str(attacker.unit_index)+","+str(attacker.player_index)+" VS "+str(target.name)+str(target.unit_index)+","+str(target.player_index)+" Roll:"+str(roll))
        if attack>=roll or roll==1:
          target.armor-=1
          self.game.logger.info(str(target.name)+" hit")
          if target.armor<=0:
            target.destroy()
            self.game.logger.info(str(target.name)+" destroyed")




