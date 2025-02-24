"""
    Prompt:
    
    Write a function shuffle() that accepts a list cards of 2n elements in the form:

    [x1, x2, ... , xn, y1, y2, ... , yn]

    Return the list in the form [x1, y1, x2, y2, ... , xn, yn].
"""

def shuffle(cards):
    n = len(cards) // 2
    shuffled = []
    
    for i in range(n):
        shuffled.append(cards[i])
        shuffled.append(cards[i + n])
    
    return shuffled


cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))