import random


class Economic_Engine:
    def __init__(self, game):
      self.game = game
      self.board = self.game.board


    def decay(self,player):
        for unit in player.units:
            if unit.exist == True and unit.name != "ShipYard" and unit.name != "Decoy" and unit.name != "Colony ship":
                if player.playerCP >= (unit.armor):
                    player.playerCP = self.playerCP - (unit.armor)
                    print(str(unit.armor))
                else:
                    unit.delete()
                    player.Game.boolean_print("Unit " + str(unit.unit_number) +
                                            " decayed")
        print(str(player.playerCP))


    def get_credits(self, planets, player):
        for planet in planets:
            if planet.player_control == player.player_num:
                #self.playerCP = self.playerCP + planet.health
                player.playerCP = self.playerCP + 20
                print(str(player.player_num))
                print(player.playerCP)
