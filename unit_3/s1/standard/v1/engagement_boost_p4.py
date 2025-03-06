"""
    Prompt:
    You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain 
    strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

    Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in 
    non-decreasing order.

    Your Task:

        * Read through the existing solution and add comments so that everyone in your pod understands how it works.
        * Modify the solution below to use the two-pointer technique.
"""

def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort()
    # print("SE", squared_engagements)
    # result = [0] * len(engagements)
    # # print(result)
    # position = len(engagements) - 1
    
    # for square, original_index in squared_engagements:
    #     result[position] = square
    #     position -= 1
    
    # print("RESULT", result)
    """
        4 -> 100
        3 -> 9
        2 -> 0
        1 -> 1
        0 -> 16
    """
    return squared_engagements

def engagement_boost_2(engagements):
    left = 0
    right = len(engagements) - 1

    while left < right:
        
        
        left += 1
        right -= 1
    

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

print(engagement_boost_2([-4, -1, 0, 3, 10]))
print(engagement_boost_2([-7, -3, 2, 3, 11]))