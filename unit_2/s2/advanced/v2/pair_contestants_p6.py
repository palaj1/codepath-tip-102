"""
    Prompt:

    In a reality TV challenge, contestants must be paired up in teams. Each team's combined score must be 
    divisible by a target number k. You are given an array of integers scores representing the scores of 
    the contestants and an integer k.

    You need to determine whether it is possible to pair all contestants such that the sum of the scores of
    each pair is divisible by k.

    Return True if it is possible to form the required pairs, otherwise return False 
"""

def pair_contestants(scores: list, k: int):
    remainder_count = dict()

    for score in scores:
        r = score % k

        if r in remainder_count:
            remainder_count[r] += 1
        else:
            remainder_count[r] = 1

    for r in remainder_count:
        if r == 0:
            if remainder_count[r] % 2 != 0:
                return False
        else:
            if remainder_count.get(r, 0) != remainder_count.get(k - r, 0):
                return False
    
    return True

scores1 = [1,2,3,4,5,10,6,7,8,9]
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3)) 