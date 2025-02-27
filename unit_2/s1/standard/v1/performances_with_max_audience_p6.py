"""
    Prompt:

    You are given an array audiences consisting of positive integers representing the audience size for
    different performances at a music festival

    Return the combined audience size of all performances in audiences with the maximum audience size.

    The audience size of a performance is the number of people who attended that paerformance
"""
from collections import Counter

def max_audience_performances(audiences):
    audience_count = Counter(audiences)
    max_audience = max(audience_count)

    return max_audience * audience_count[max_audience]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))