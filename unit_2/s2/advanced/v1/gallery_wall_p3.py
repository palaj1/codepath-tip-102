"""
    Prompt:
    
    You are tasked with organizing a collection of art prints represented by a list of strings collection.
    You need to display these prints on a single wall in a 2D array format that meets the following
    criteria:
    
        1. The 2D array should contain only the elements of the array collection
        2. Each row in the 2D array should contain distinct strings
        3. The number of rows in the 2D array should be minimal
    
    Return the resulting array, if there are multiple answers, return any of them.

    Note that the 2D array can have a different number of elements on each row.
"""


from collections import Counter

def organize_exhibition(collection: list):
    freq_dict = Counter(collection)
    num_sublists = max(freq_dict.values())
    
    if num_sublists == 1:
        return [collection]
    
    sublists = [[] for _ in range(num_sublists)]

    for s in sublists:  
        for c in collection:
            if freq_dict[c] >= 1 and c not in s:
                s.append(c)
                freq_dict[c] -= 1

    return sublists


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))