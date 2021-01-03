import random


class Economic_Engine:
    def __init__(self, game):
      self.game = game
      self.board = self.game.board


    def decay(self,player):
        for unit in player.units:
            if unit.exist == True and unit.name != "ShipYard" and unit.name != "Decoy" and unit.name != "Colony ship":
                if player.playerCP >= (unit.armor):
                    player.playerCP = player.playerCP - (unit.armor)
                    # print(str(unit.armor))
                else:
                    unit.delete()
                    player.Game.boolean_print("Unit " + str(unit.unit_number) +
                                            " decayed")


    def get_credits(self, planets, player):
        for planet in planets:
            if planet.player_control == player.player_num:
                player.playerCP = player.playerCP + 20

