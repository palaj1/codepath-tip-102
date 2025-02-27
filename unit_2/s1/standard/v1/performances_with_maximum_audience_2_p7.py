"""
    Prompt:
    
    If you used a dictionary as part of your solution to max_audience_perfomances() in the previous
    problem, try reimplementing the function without using a dictionary. If you implemented 
    max_audience_performances() without using a dictionary, try solving the problem with a dictionary.

    Once you've come up with your second solution, compare the two. 
    
    Is one solution better than the other? Why or why not?
"""

def max_audience_performances(audiences):
    max_key = 0
    multiplier = 1

    for s in audiences:
        if s > max_key:
            max_key = s
            multiplier = 1
        elif s == max_key:
            multiplier += 1
    
    return max_key * multiplier

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))