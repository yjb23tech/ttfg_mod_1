import random 

class Weapon:
    
    def __str__(self):
        return (f"The {self.str_name} is {self.str_msg}; this weapon has an attack power of {self.int_atk_pwr} - happy hunting")

class BattleAxe(Weapon):

    def __init__(self):

        self.str_name = "Battle Axe"
        self.str_msg = "perfect for large area of effect style attacks"

        self.int_atk_pwr = random.randint(110, 120)

class LongSword(Weapon):

    def __init__(self):

        self.str_name = "Long Sword"
        self.str_msg = "deadly in close quarters and capable of levelling all foes in the immediate vicinity"

        self.int_atk_pwr = random.randint(110, 120)
    



