class Player:
    def __init__(self,p_index,player_strat,innit_pos,game):
      self.player_index=p_index
      self.strat=self.init_strat(player_strat,p_index)
      #init home colony
      self.game=game
      self.units=[]
