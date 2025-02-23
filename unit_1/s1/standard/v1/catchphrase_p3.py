"""
    Prompt: 
    
    Write a function print_catchphrase() that accepts a string character as a parameter
    and prints the catchphrase of the given character as outlined below:

    
    "Pooh" -> "Oh bother!"
    "Tigger" -> "TTFN: Ta-ta for now!"
    "Eeyore" -> "Thanks for noticing me."
    "Christopher Robin" -> "Silly old bear"

    if the given character does not match one of the characters included above, print
    "Sorry! I don't know <character>'s catchphrase!"
"""

def print_catchphrase(character):
    match character:
        case "Pooh":
            print("Oh bother!")
        case "Tigger":
            print("TTFN: Ta-ta for now!")
        case "Eeyore":
            print("Thanks for noticing me.")
        case "Christopher Robin":
            print("Silly old bear")
        case _:
            print(f"Sorry! I don't know {character}'s catchphrase!")
    
print_catchphrase("Pooh")
print_catchphrase("Tigger")
print_catchphrase("Eeyore")
print_catchphrase("Christopher Robin")
print_catchphrase("Jaime")