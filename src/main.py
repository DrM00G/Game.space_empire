from game import Game

game = Game(True)
game.generate()
game.state()
game.run_to_completion(3)
game.show_winner()