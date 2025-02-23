"""
    Prompt:
    
    Rabbit is very particular about his belongings to own an even number of
    each thing he owns. Write a function can_pair() that accepts a list of 
    integers item_quantities. Return True if each number in item_quantities
    is even. Return False otherwise.
"""

def can_pair(item_quantities):
    return not any(e % 2 != 0 for e in item_quantities)


item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))
item_quantities.append(9)
print(can_pair(item_quantities))
def_item_quantities = [1] * 9
print(can_pair(def_item_quantities))

