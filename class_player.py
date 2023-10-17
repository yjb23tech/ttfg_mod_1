class Player:

    def __init__(self):

        self.str_name = "Yuri Orlov"
        self.str_place_of_birth = "Odessa"
        self.str_msg = "peace is bad for business"
    
    def __str__(self):

        return (f"My name is {self.str_name}; always remember: {self.str_msg}")

