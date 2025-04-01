"""
    Prompt:

    The sequence team, The Fantastic Four, are training to increase their power levels. Their
    power level is represented as a power of 4. Write a recursive function that calculates the 
    power of 4 raised to the nth power to determine their training level.

    Ealuate the time complexity of your solution. Define your variables and provide a rationale
    for why you believe your solution has the stated time complexity.
"""

# output should always be positive
def power_of_four(n: int):
    if n == 0:
        return 1
    
    if n < 0:
        return power_of_four(-n)

    return 4 * power_of_four(n - 1)


print(power_of_four(2)) # expected output: 16
print(power_of_four(-2)) # expected output: 16