from class_weapon import Weapon, BattleAxe, LongSword 

class Player:

    def __init__(self):

        self.str_name = "Yuri Orlov"
        self.str_place_of_birth = "Odessa"
        self.str_msg = "peace is bad for business"

        self.arr_inventory = [BattleAxe(), LongSword()]
        self.obj_current_weapon = None 
    
    def __str__(self):

        return (f"\nMy name is {self.str_name}; always remember: {self.str_msg}")
    
    def display_inventory(self):

        print("\nIn your inventory you have access to the following weapons:")
        for x, weapon in enumerate(self.arr_inventory, 1):
            print(f"{x}. {weapon}")
    
    def display_current_weapon(self):

        if self.obj_current_weapon == None:
            print(f"\n{self.str_name} is currently unarmed - this is dangerous!\n")
        else:
            print(f"\n{self.str_name} is currently armed - you are dangerous XD\n")
    

    


