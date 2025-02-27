"""
    Prompt:

    You are given an array of strings performer_names, and an array performance_items that consists of 
    distinct positive integers representing the performance durations in minutes. Both arrays are of
    length n.

    For each index i, performer_names[i] and performance_times[i] denote the name and performance duration
    of the ith performer.

    Return performer_names sorted in descending order by the performance durations.
"""

def sort_performers(performer_names: list, performance_times: list):
    sorted_performers = sorted(zip(performer_names, performance_times), key=lambda p: p[1], reverse=True)
    return [name for name, _ in sorted_performers]


performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))