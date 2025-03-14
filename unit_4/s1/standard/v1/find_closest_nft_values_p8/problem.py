"""
    Prompt:

    Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of NFT
    values and a budget, you need to find the two NFT values that are closest to the given budget: one 
    that is just below or equal to the budget and one that is just above or equal to the budget. If an 
    exact match exists, it should be included as one of the values.

    Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget, 
    and returns the pair of the two closest NFT values.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
    for why you believe your solution has the stated time and space complexity.
"""

# Brute Force Approach
# Time complexity O(n) and space complexity O(1)
#   * TC - iterates through the entire list of "nft_values"
#   * SC - although I do use two pointer variables, they aren't considered a data structure, so it would be constant time
def find_closest_nft_values(nft_values, budget):
    # if budget is between two exsting values in "nft_values", return (i - 1, i + 1)
    # If budget is in "nft_values", return (0, budget)

    n = len(nft_values)
    l_pointer = 0
    r_pointer = 2

    while r_pointer < n:
        if nft_values[r_pointer] < budget:
            l_pointer += 1
            r_pointer += 1
            continue
        
        if nft_values[r_pointer - 1] == budget:
            return (0, budget)
        
        if nft_values[r_pointer - 1] < budget:
            return (nft_values[r_pointer - 1], nft_values[r_pointer])

        if nft_values[r_pointer - 1] > budget:
            return (nft_values[l_pointer], nft_values[r_pointer - 1]) 


    if nft_values and (nft_values[0] < budget and nft_values[1] > budget):
        return (nft_values[0], nft_values[1])
    
    return (None, None)


# Binary Search Approach
# Time complexity O(log n) and space complexity O(1)
#   * TC - each step is halved, allowing us to only prioritize the case where we've found an exact match or we have gone over the limit or under
#   * SC - although I do use two pointer variables, they aren't considered a data structure, so it would be constant time
def find_closest_nft_values_2(nft_values, budget):
    if not nft_values:
        return (None, None)
    
    n = len(nft_values)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if nft_values[mid] == budget:
            return (0, nft_values[mid])
        elif nft_values[mid] < budget:
            left += mid + 1
        else:
            right = mid - 1

    lower = nft_values[right] if right >= 0 else None
    upper = nft_values[left] if left < n else None

    return (lower, upper)

# =================================== Approach #1 ===================================
print("========================== Brute Force Approach (Two-Pointer)==========================")
nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]


print(find_closest_nft_values(nft_values, 8.0)) # -> (7.2, 9.0)
print(find_closest_nft_values(nft_values_2, 6.5)) # -> (6.3, 7.8)
print(find_closest_nft_values(nft_values_3, 3.0)) # ->(2.5, 4.0)

# Extra Precautions
nft_values_4 = []
nft_values_5 = [1.0, 2.0]

print(find_closest_nft_values(nft_values_4, 5.0)) # -> (None, None)
print(find_closest_nft_values(nft_values_5, 5.0)) # -> (1.0, 2.0)
print(find_closest_nft_values(nft_values_5, 1.5)) # -> (1.0, 2.0)
print(find_closest_nft_values(nft_values_3, 4.0)) # ->(2.5, 4.0)


# =================================== Approach #2 ===================================
print("========================== Binary Search Approach ==========================")
print(find_closest_nft_values_2(nft_values, 8.0)) # -> (7.2, 9.0)
print(find_closest_nft_values_2(nft_values_2, 6.5)) # -> (6.3, 7.8)
print(find_closest_nft_values_2(nft_values_3, 3.0)) # ->(2.5, 4.0)

print(find_closest_nft_values_2(nft_values_4, 5.0)) # -> (None, None)
print(find_closest_nft_values_2(nft_values_5, 5.0)) # -> (2.0, None)
print(find_closest_nft_values_2(nft_values_5, 1.5)) # -> (1.0, 2.0)
print(find_closest_nft_values_2(nft_values_3, 4.0)) # ->(2.5, 4.0)