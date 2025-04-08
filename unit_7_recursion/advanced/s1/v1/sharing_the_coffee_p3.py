"""
    Prompt:

    The deli staff is in desperate need of caffeine to keep them going through their shift 
    and has decided to divide the coffee equally among themselves. Each batch of coffee is 
    stored in containers of different sizes. Write a function can_split_coffee() that accepts 
    a list of integers 'coffee' representing the volume of each batch of coffee and returns 
    'True' if the coffee can be split evenly by volume among 'n' staff and 'False' otherwise.

    Evaluate the time and space complexity of your solution. Define your variables and 
    provide a rationale for why you believe your solution has the stated time and space 
    complexity.
"""

# The time complexity here would be O(n) because we parse the entire list of coffee batches
# The space complexity here would be O(1) because there isn't any intializations
def can_split_coffee(coffee, n):
    if not coffee:
        return True
    
    if coffee[0] % n != 0:
        return False

    return can_split_coffee(coffee[1:], n)

print(can_split_coffee([4, 4, 8], 2)) # True
print(can_split_coffee([5, 10, 15], 4)) # False