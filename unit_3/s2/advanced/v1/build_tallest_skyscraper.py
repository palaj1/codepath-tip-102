"""
    Prompt:

    You are given an array 'floors' representing the heights of different building floors. Your task is
    to design a skyscraper using these floors, where each floor must be placed on top of a floor with equal
    or greater height. However, you can only start a new skyscraper when necessary, meaning when no more 
    floors can be addded to the current skyscraper according to the rules.

    Return the number of skyscraper you can build using the given floors
"""

def build_skyscrapers(floors):
    skyscrapers_stack = []

    for floor in floors:
        if skyscrapers_stack and skyscrapers_stack[-1] < floor:
            skyscrapers_stack.pop()

        skyscrapers_stack.append(floor)

    return len(skyscrapers_stack)

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))