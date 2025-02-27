"""
    Prompt:

    Given two lists of strings artists and set_times of length n, write a function lineup()
    that maps each artist to their set time.

    An artist artists[i] has set time set_times[i]. 
    
    Assume i <= 0 < n and len(artists) == len(set_times)
"""

def lineup(artists, set_times):
    if len(artists) != len(set_times):
        raise ValueError("Both artists and set_times should be of same length")

    return {artists[i]: set_times[i] for i in range(len(artists))}


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))