"""
    Prompt: 

    Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify 
    their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n]

    The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1
    containing the integers from 1 to n - 1 exactly once. and the integer n twice. 

    For example:
        base[1] = [1, 1] 

        base[3] = [1, 2, 3, 3]

    Write a function is_authentic_collection that accepts an array of integers act_pieces and returns True
    if the given array is an authentic array, and otherwise returns False 

    Note: A permutation of integers represents an arrangement of these numbers.
    
    For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3 
"""

from collections import Counter

def is_authentic_collection(art_pieces: list):
    art_pieces_dict = Counter(art_pieces)

    for i in range(1, len(art_pieces) - 2):
        if art_pieces_dict[i] != 1:
            return False
 
    return art_pieces_dict[len(art_pieces) - 1] == 2



collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))