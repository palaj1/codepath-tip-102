"""
    Prompt:

    Tony Stark, aka Iron Man has designed many different suits over the years.

    Given a list of strings 'suits' where each string is a suit in Stark's collection, count
    the total number of suits in the list.

        1. Implement the solution iteratively without the use of the len() function
        2. Implement the solution recursively
        3. Discuss what are the similarities between the two solutions? What are the 
           differences?
"""

def count_suits_iterative(suits):
    count = 0
    
    for _ in suits:
        count += 1
    
    return count

def count_suits_recursive(suits: list):
    if not suits:
        return 0
    
    suits.pop()

    return count_suits_iterative(suits) + 1

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
print(count_suits_recursive([]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III", "Mark IV", "Mark V"]))
