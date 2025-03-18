"""
    Prompt:

    In Animal Crossing, as players become friends with villagers, villagers might as the player to suggest
    a ew catchphrase.

    Adding on to your existing code, update 'bones' so that his catchphrase is "ruff it up" instead of its 
    current value, "yip yip".

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

print(bones.catchphrase)

bones.catchphrase = "ruff it up"

print(bones.catchphrase)

