from objets.thePriceIsRigth import ThePriceIsRigth
from objets.graphiqueInterface import GameInterface

# On ne crée plus l'objet logic ici, car GameInterface le crée lui-même dans son __init__
app = GameInterface()

# On lance la fenêtre
app.mainloop()