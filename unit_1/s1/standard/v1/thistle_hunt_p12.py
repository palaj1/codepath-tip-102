"""
    Prompt:

    Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write
    a function locate_thistles() that takes in a list of strings items and returns a list
    of the indices of any elements with value "thistle". The indices in the resulting list
    should be ordered from least to greatest.
"""

def locate_thistles(items):
    target = "thistle"
    return [i for i, val in enumerate(items) if val == target]

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))
items.extend(["thistlee", "thistl", "thistle"])
print(locate_thistles(items))