"""
    Prompt:

    Implement a function get_item() that accepts a 0-indexed list items
    and a non-negative integer x and returns the element at index x in items.
    If x is not valid index of items, return None
"""

def get_item(items, x):
    if x < 0 or len(items) == 0 or x > len(items):
        return None

    return items[x]



clothing_brands = ["Adidas", "Wrangler", "Lee", "AG Jeans", 
                   "G-Star RAW", "Levi's"]

print(get_item(clothing_brands, 0))
print(get_item(clothing_brands, 3))
print(get_item(clothing_brands, 5))
print(get_item(clothing_brands, 7))
