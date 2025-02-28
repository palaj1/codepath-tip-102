"""
    Prompt:

    You are given two strings s and t representing the stage arrangements of performers in two different
    performances at a music festival, such that every performer occurs at most once in s and t, and t is
    a permutation of s

    The stage arrangement difference between s and t is defined as the sum of the absolute difference 
    between the index of the occurrence of each performer in s and the index of the occurrence of the 
    same performer in t.

    Return the stage arrangement difference between s and t.

    A permutation is a rearrangement of a sequence. 

    For example:
        [3, 1, 2] and [2, 1, 3] are both permutations of the list [1, 2, 3]
"""
def find_stage_arrangement_difference(s: list, t: list):
    index_map = {char: i for i, char in enumerate(s)}                                                   
    print(index_map)
    return sum(abs(i - index_map[char]) for i, char in enumerate(t))


s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))