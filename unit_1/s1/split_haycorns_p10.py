"""
    Prompt:
    Piglet's has collected a big pile of his favorite food, haycorns, and 
    wants to split them evenly amongst hist friends. Write a function 
    split_haycorns() to help Piglet determine the number of ways he can 
    split his haycorns into even groups. split_haycorns() accepts a positive
    integer quantity as a parameter and returns a list of all divisors of
    quantity.
"""

def split_haycorns(quantity):
    divisors = set()
    # Given that n is a divisor of quantity, then quantity // n is also a divisor
    for n in range(1, int(quantity ** 0.5) + 1):
        if quantity % n == 0:
            divisors.add(n)
            divisors.add(quantity // n)
    return sorted(divisors)

print(split_haycorns(6))