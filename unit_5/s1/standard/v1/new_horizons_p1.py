"""
    Prompt:

    Step 1: Copy the following code into your IDE
    
    Step 2: Instantiate an instance of the class 'Villager', which represents characters in Animal Crossing.
    Store the instance in a variable naed 'apollo'

        * The 'Villager' object created should have the name "Apollo", the species "Eagle", and 
        catchphrase "pah"
"""

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")

# Instantiate your villager here
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 