import random 
class ThePriceIsRigth:
    def __init__(self, max_price=100):
        self.target_price = random.randint(1, max_price)
        self.attempts = 0
        self.max_attempts = 10
        self.is_game_over = False
    def check(self, proposal):
        self.attempts += 1
        if proposal < self.target_price:
            status = 2
        elif proposal > self.target_price:
           status= 1
        else:
           status = 0
        if self.attempts >= self.max_attempts and status != 0:
            status = -1
            self.is_game_over = True
        return status
    def display_message(self, status):
        if status == 2:
            print(f"More expensive ! test {self.attempts} / {self.max_attempts}")
        elif status == 1:
            print(f"Cheaper !test {self.attempts} / {self.max_attempts}")
        elif status == 0:
            print(f"Win ! after {self.attempts} test")
        elif status == -1:
            print(f"Lost the game, the rigth price is {self.target_price} $")
    def inputPrice (self):
        if not self.is_game_over: 
            price = input("What is your price?")
            try:
                price = int(price)
                status = self.check(price)
                self.display_message(status)
            except ValueError:
                print("Please enter a valid number")