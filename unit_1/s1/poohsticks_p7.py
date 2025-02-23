"""
    Prompt:

    Winnie the Pooh and his friends are playing a game called Poohsticks
    where they drop sticks in a stream and race them. They time how long
    it takes each player's stick to float under Poohsticks Bridge to score
    each round.

    Write a function count_less_than() to help Pooh and his friends determine
    how many players should move on to the next round of Poohsticks 
    count_less_than() should accept a list of integers race_times and an
    integer threshold and return the number of race times less than threshold.
"""

def count_less_than(race_times, threshold):
    return list(filter(lambda x: x < threshold, race_times))

race_times = [1, 2, 3, 4, 5, 6]

print(count_less_than(race_times, 4))