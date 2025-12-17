from objets.thePriceIsRigth import ThePriceIsRigth

game = ThePriceIsRigth()
print("--- Welcome to The Price Is Right ---")
while not game.is_game_over:
    game.inputPrice()