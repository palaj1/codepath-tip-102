"""
    Prompt:

    You have a list of integers collection_sizes representing the sizes of different art 
    collections in your gallery and are trying to determine how to group them best fit in
    your space. Given an integer k write a function count_divisible_collection() that 
    returns the number of non-empty subarrays (contiguous parts of the array) where the 
    sum of the sizes is divisible by k
"""
from collections import Counter, defaultdict

# Prefix Sum Approach O(N)
#   * uses a HashMap of (r:c) pairs, where 'r' = remainder  and 'c' = count
#          - simulates the sum of an array from i to j
#   * when two prefix_sums have the same remainder modulo k, the sum of the subarray between
#     them is divisible by k.
def count_divisible_collections(nums: list, k: int):
    remainder_count = {0: 1}  
    prefix_sum = 0
    result = 0
    
    for num in nums: 
        prefix_sum += num
        
        remainder = prefix_sum % k
        
        if remainder in remainder_count:
            result += remainder_count[remainder]
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1
    
    return result






nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5, 10]
k2 = 5

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))
