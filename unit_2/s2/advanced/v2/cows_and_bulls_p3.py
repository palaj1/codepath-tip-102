"""
    Prompt:

    In a reality Tv show, contestants play a mini-game called Bulls and Cows for a price. The objective
    is to guess a secret number within a limited number of attempts. You, as the host, need to provide 
    hints to the contestants based on their guesses.

    When a contestant makes a guess, you provide a hint with the following information.
        
        * The number of "bulls," which are digits in the guess that are in the correct position
        * The number of "cows," which are digits in the guess that are in the secret number but are located
          in the wrong position.

    Given the secret number "secret" and the contestant's guess "guess", return the hint for their guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
    Note that both "secret" and "guess" may contain duplicate digits
"""
from collections import Counter

def get_hint(secret: str, guess: str):
    cows = 0
    bulls = 0 

    secret_remaining_freq = Counter(secret)

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            cows += 1
            # Decrease count for exact match (cow)
            secret_remaining_freq[secret[i]] -= 1

            if secret_remaining_freq[secret[i]] == 0:
                del secret_remaining_freq[secret[i]]

    for i in range(len(guess)):
        if secret[i] != guess[i]:
            if guess[i] in secret_remaining_freq and secret_remaining_freq[guess[i]] > 0:
                bulls += 1
                secret_remaining_freq[guess[i]] -= 1
                
                if secret_remaining_freq[guess[i]] == 0:
                    del secret_remaining_freq[guess[i]]

    return "{a}A{b}B".format(a=cows, b=bulls)


secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))
        