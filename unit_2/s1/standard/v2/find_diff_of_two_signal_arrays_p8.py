"""

    Prompt:

    If you used a dictionary sas part of your solution to max_audience_performances() in the previous
    problem, try reimplementing the function without using a dictionary. If you implemented
    max_audience_performances() without using a dictionary, try solving the problem with a dictionary

    Once you've come up with your second solution, compare the two. Is one solution better than the other?
    Why or why not?

    Approach #1
        first turn them into sets()
        substract the sets -> display the diff

    Approach #2
        loop through both lists finding the distinct elements

"""

def find_difference(signals1, signals2):
    signals1_set = set(signals1)
    signals2_set = set(signals2)

    return [signals1_set - signals2_set, signals2_set - signals1_set]

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3] 
signals2_example2 = [1, 1, 2, 2]


def find_difference_2(signals1, signals2):
    signals1_set = set(signals1)
    signals2_set = set(signals2)

    d1_l = []
    for s in signals1_set:
        if s not in signals2_set:
            d1_l.append(s)

    d2_l = []
    for s in signals2_set:
        if s not in signals1_set:
            d2_l.append(s)

    return [d1_l, d2_l]


print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))
print(find_difference_2(signals1_example1, signals2_example1)) 
print(find_difference_2(signals1_example2, signals2_example2))