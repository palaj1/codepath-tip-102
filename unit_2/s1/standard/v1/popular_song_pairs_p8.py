"""
    Prompt:

    Given an array of integers popularity_scores representing the popularity scores of songs in a music
    festival playlist, return the number of popular song pairs

    A pair (i, j) is called popular if the songs have the same popularity score and i < j

    Hint: number of pairs (n * n - 1) / 2
"""
from collections import Counter

def num_popular_pairs(popularity_scores):
    score_count = Counter(popularity_scores)
    pairs = 0

    for count in score_count.values():
        if count > 1:
            pairs += (count * (count - 1)) // 2
    return pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 
print(num_popular_pairs(popularity_scores1))
_