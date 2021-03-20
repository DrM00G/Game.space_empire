import random
import math

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
          self.rolls.append(math.ceil(10*random.random()))
      else:
        self.rolls=[n+1 for n in range(self.sided_die)]
        if self.die_mode=="decending":
          self.rolls=self.rolls[::-1]

    def locate_combat(self):
      combat_dict={}
      for coord in self.board.board_dict:
        if len(self.board.board_dict[coord]["units"])>1:
          player_count=[[],[]]
          for unit in self.board.board_dict[coord]["units"]:
            player_count[unit.player_index].append(unit.name)
          if len(player_count[0])!=0 and len(player_count[1])!=0:
            if player_count[0]==["Colony"] or player_count[1]==["Colony"]:
              combat_dict[coord]={}
              combat_dict[coord]= [
              {"type": unit.name,"player":unit.player_index,
              "num":unit.unit_index,'tactics':unit.tactics,
              "coords":unit.coords,
              "technology":{"defense": unit.defense,"attack": unit.attack,"movement": unit.movement},
              "hits_left":unit.armor,
              'turn_created':unit.turn_made
              }for unit in self.combat_order(coord) if unit.exists==True]
            else:
              combat_dict[coord]={}
              combat_dict[coord]= [
              {"type": unit.name,"player":unit.player_index,
              "num":unit.unit_index,'tactics':unit.tactics,
              "coords":unit.coords,
              "technology":{"defense": unit.defense,"attack": unit.attack,"movement": unit.movement},
              "hits_left":unit.armor,
              'turn_created':unit.turn_made
              }for unit in self.combat_order(coord) if unit.exists==True and unit.name!= "Colony"] 
      return combat_dict


    def kill_bystanders(self,combat_state):
        for coord in combat_state:
          units=[unit for unit in self.board.board_dict[coord]["units"]]
          for unit in units:
            if unit.combat_ready != True:              
              unit.destroy()

    def combat_order(self,coord):
        order=[]
        for unit in self.board.board_dict[coord]["units"]:
            order.append(unit)
        return sorted(order,key = lambda unit:(unit.tactics,-unit.player.player_index,-unit.unit_index),reverse=True)

    def complete_combat_phase(self):
        self.kill_bystanders(self.locate_combat())
        if len(self.locate_combat())>0:
            self.game.log("Combat Locations:")
        for key in self.locate_combat():
            for unit in self.combat_order(key):
                self.game.log("Player "+str(unit.player_index)+" "+str(unit.name)+" "+str(unit.unit_index))
        next_coord=[key for key in self.locate_combat()][0]
        while len(self.locate_combat())>0 and self.game.winner==None:
          combat_coord=[key for key in self.locate_combat()][0]
          if(len(self.locate_combat())==next_coord):
            self.game.log("Combat at "+str(next_coord))
            if len(self.locate_combat())>1:
                next_coord=[key for key in self.locate_combat()][1]
            else:
                next_coord=None
          #SCREAN
          order = self.combat_order(combat_coord)
          for unit in order:
            if unit.exists and combat_coord in [key for key in self.locate_combat()] and self.game.winner==None and unit.name!="Colony":
              target=unit.player.strat.decide_which_unit_to_attack(self.locate_combat()[combat_coord], combat_coord,unit.name,unit.unit_index)
            #   print(target)
              enemy="no" 
              for vs_unit in self.combat_order(combat_coord):
                if vs_unit.unit_index==target["number"] and vs_unit.player_index!=unit.player_index:
                  enemy=vs_unit
              if enemy != "no":
                self.do_combat(unit,enemy)
        for player in self.game.players:
          player.update_indexes()

    def do_combat(self,attacker,target):
        if len(self.rolls) == 0:
          self.roll_die()
        roll=self.rolls[0]
        self.rolls.remove(roll)
        attack=attacker.attack-target.defense
        self.game.log(str(attacker.name)+str(attacker.unit_index)+","+str(attacker.player_index)+" VS "+str(target.name)+str(target.unit_index)+","+str(target.player_index)+" Roll:"+str(roll)+" Threshold:"+str(attack))
        if attack>=roll or roll==1:
          target.armor-=1
          self.game.log(str(target.name)+" hit")
          if target.armor<=0:
            target.destroy()
            self.game.log(str(target.name)+" destroyed")




