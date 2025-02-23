"""
    Prompt:

    Signs in the Hundred Acre Wood have been losing letters as Tigger
    bounces around stealing any letters he needs to spell out his name.
    Write function tiggerfy() that accepts a string s, and returns a new
    string with letters t, i, g, e, and r from it.
"""

def tiggerfy(s):
    # if "word" were to be large, a set(word) would be much more efficient
    word = "tiger"
    return ''.join(c for c in s if c.lower() not in word)

print(tiggerfy("suspicerous"))
print(tiggerfy("Trigger"))
print(tiggerfy("Hunny"))


