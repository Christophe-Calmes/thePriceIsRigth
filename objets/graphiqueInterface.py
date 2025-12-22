import customtkinter as ctk
from objets.thePriceIsRigth import ThePriceIsRigth # Vérifie bien la majuscule ici

class GameInterface(ctk.CTk):
    def __init__(self):
        super().__init__() 
        
        self.game_logic = ThePriceIsRigth()
        
        self.title("The Price is Right")
        self.geometry("400x300")

        self.entrer_price = ctk.CTkEntry(self, placeholder_text="The price is....")
        self.entrer_price.pack(pady=10)
        
        self.button = ctk.CTkButton(self, text="Check !", command=self.handle_click)
        self.price = ctk.CTkEntry(self)
        self.button.pack(pady=20)
        
        self.label_result = ctk.CTkLabel(self, text="Good luck !", font=("Arial", 16))
        self.label_result.pack(pady=20)

    def handle_click(self):
        if not self.game_logic.is_game_over:
            thePiceIs = self.entrer_price.get()
            try:
                    price_player = int(thePiceIs)
                    status = self.game_logic.check(price_player)
                    message = self.game_logic.display_message(status)
                    self.label_result.configure(text=message)
                    self.price_player.delete(0, 'end')
                    if self.game_logic.is_game_over:
                        self.button.configure(state="disabled", text="End game")
            except ValueError:
               
                self.label_result.configure(text="Error : Number only please !")