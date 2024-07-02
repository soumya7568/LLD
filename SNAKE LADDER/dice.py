import random

class Dice:
    def __init__(self,count) -> None:
        self.count = count
        
    def roll_dice(self):
        total = 0
        for i in range(self.count):
            curr = random.randint(1,6)
            total+=curr
        return total