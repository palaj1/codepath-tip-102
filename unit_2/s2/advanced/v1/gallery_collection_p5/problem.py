"""
    Prompt:

    Your gallery has entered a competition for the most beautiful collection. Your collection is represented
    by a string collection where each artist in your gallery represented by a character. The beauty
    of a collection is defined as the difference in frequencies between the most frequent and the least 
    frequent characters.

        * For example, the beauty of "abaacc" is 3 - 1 = 2
    
    Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its 
    substrings (sub-collections), not just of the collection itself
"""

def beauty_sum(collection: str):
    n = len(collection)
    total_beauty = 0

    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[collection[j]] = freq.get(collection[j], 0) + 1

            max_freq = max(freq.values())
            min_freq = min(freq.values())
            beauty = max_freq - min_freq

            total_beauty += beauty

    return total_beauty
    


print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

