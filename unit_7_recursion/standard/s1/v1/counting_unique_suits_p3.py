"""
    Prompt:

    Some of Iron Man's suits are duplicates.

    Given a list of strings 'suits' where each string is a suit in Stark's collection, 
    count the total number of unique suits in the list.

        1. Implement the solution iteratively
        2. Implement the solution recursively
        3. Discuss: what are the similarities between the two solutions? 
           What are the differences?
        4. Evaluate the time complexity of each solution. Are they the same? Define
           your variables and provide a rationale for why you believe your solution
           has the states time complexity.
"""

def count_suits_iterative(suits: list):
    unique_elements = set()

    for suit in suits:
        unique_elements.add(suit)


    return len(unique_elements)

def count_suits_recursive(suits: list):
    if not suits:
        return 0
    
    if len(suits) == 1:
        return 1
    
    current_suit = suits[0]
    remaining_suits = suits[1:]
    current_suit_count = remaining_suits.count(current_suit)
    
    if current_suit_count >= 1:
        return count_suits_recursive(remaining_suits) 

    return count_suits_recursive(remaining_suits) + 1

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"])) # expected output = 3
print(count_suits_iterative(["Mark I", "Mark I", "Mark II", "Mark III"])) # expected output = 3
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"])) # expected output = 2
print(count_suits_recursive(["Mark I", "Mark I", "Mark II", "Mark III"])) # expected output = 3
