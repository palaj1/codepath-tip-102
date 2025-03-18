"""
    Prompt:

    Step 1: Using 'Villager' class from Problem 1, add the following greet_player() metehod to your 
    existing code:
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    Step 2: Create a second instance of 'Villager' in a variable named 'bones'.
        
        * The 'Villager' object created should have 'name' "Bones", 'species' "Dog", and 'catchphrase' 
          "yip yip"

    Step 3: Call the method greet_player() with your name and print out:
        
        "Bones: Hey there, <your name>! How's it going, yip yip!"
"""

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
bones = Villager("Bones", "Dog", "yip yip")

print(bones.greet_player("Tram"))
