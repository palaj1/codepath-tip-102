"""
    Prompt:

    T-I-Double Guh-Er: That spells Tigger! 

    Write a function tiggerfy() that accepts a string word and returns a new string that
    removes any substrings t, i, gg, and er from word.

    The function should be case insensitive.
"""

def tiggerfy(word: str):
    word = word.lower()

    substrings = ['t', 'i', 'gg', 'er']

    for substr in substrings:
        word = word.replace(substr, '')

    return word

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
