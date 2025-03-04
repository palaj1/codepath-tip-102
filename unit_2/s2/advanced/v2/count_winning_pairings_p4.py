"""
    Prompt:

    In a popular reality TV show, contestants pair up for various challenges. The pairing is considered 
    winning if the sum of their "star power" is a power of two.

    You are given an array of integers star_power where star_power[i] represents the star power of the i-th
    contestant.

    Return the number of different winning pairings you can make from the list, modulo 10^9 + 7

    Note that contestants with different indices are considered different even if they have the same star
    power.
"""
MOD = 10**9 + 7

# Brute Force Approach
def compute_powers_of_two(lst):
    max_power = 2 * max(lst)

    output = set()
    power = 1

    while power <= max_power:
        output.add(power)
        power *= 2
    
    return output

def count_winning_pairings(star_power):
    powers_of_two = compute_powers_of_two(star_power)
    n = len(star_power)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            sum_power= star_power[i] + star_power[j]
            if sum_power in powers_of_two:
                count += 1
        
    return count % 10**9

# =====================================================================
from collections import Counter

# Optimized Approach with Dictionaries
def count_winning_pairings_1(star_power: list):
    powers_of_two = compute_powers_of_two(star_power)
    freq_map = Counter(star_power)
    count = 0

    for power in star_power:
        # Decrement since we're considering the ith contestant
        freq_map[power] -= 1

        # Loop through possible powers of two, to compute complement, which will allow fast lookups to pair count
        for p in powers_of_two:
            complement = p - power
            
            if complement in freq_map:
                count += freq_map[complement]

        # On every iteration to prevent overflow 
        count %= MOD

    return count


star_power1 = [1, 3, 5, 7, 9, 20]
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))

# ============================================

star_power1 = [1, 3, 5, 7, 9, 20]
print(count_winning_pairings_1(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings_1(star_power2))