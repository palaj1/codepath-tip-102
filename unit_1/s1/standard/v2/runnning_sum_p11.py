"""
    Prompt:

    Write a function running_sum() that accepts a list of integers superhero_stats 
    representing the number of crimes Batman has stopped each month in Gotham City. The 
    function should modify the list to return the running sum such that:

    superhero_stats[i] = sum(superhero_stats[0]..superhero_stats[i]). 
    
    You must modify the list in place; you may not create any new lists as part of your 
    solution.
"""

def running_sum(superhero_stats):
    for i in range(1, len(superhero_stats)):
        superhero_stats[i] += superhero_stats[i - 1]

    return superhero_stats


superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))