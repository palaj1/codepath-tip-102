"""
    Prompt:

    In reality TV show, contestants are challenged to do the best recreation of a meal cooked by an
    all-star judge using limited resources. The meal they must recreate is represented by the string 
    target_meal. The contestants are given a collection of ingredients represented by the string 
    ingredients.

    Help the contestants by writing a function max_attempts() that returns the maximum number of copies
    of target_meal they can create using the given ingredients. You can take some letters from 
    ingredients and rearrange them to form new strings.
"""
from collections import Counter

def max_attempts(ingredients, target_meal):
    ingredients_count = Counter(ingredients)
    target_count = Counter(target_meal)

    min_meals = float('inf')

    for char, count in target_count.items():
        if char in ingredients_count:
            min_meals = min(min_meals, ingredients_count[char] // count)
        else:
            return 0

    return min_meals

ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"

print(max_attempts(ingredients1, target_meal1))
print(max_attempts(ingredients2, target_meal2))
print(max_attempts(ingredients3, target_meal3))