"""
    Prompt:

    Thanos is collecting Infinity Stones.

    Given an array of integers 'stones' representing the power of each stone, return the total
    power using a recursive approach.

    Evaluate the time complexity of your solution. Define your variables and provide a rationale
    for why you beleive your solution has the stated time complexity.
"""

def sum_stones(stones: list):
    if not stones:
        return 0
    
    current_val = stones.pop()

    return current_val + sum_stones(stones)

print(sum_stones([5, 10, 15, 20, 25, 30])) # expected output = 105
print(sum_stones([12, 8, 22, 16, 10])) # expected output = 68