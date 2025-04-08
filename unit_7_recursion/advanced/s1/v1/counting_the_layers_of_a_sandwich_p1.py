"""
    Prompt:

    You're working at a dely, and need to count the layers of a sandwich to make sure you made
    the order correctly.

    Each layer is represented as a nested list. Given a list of lists 'sandwhich' where each 
    list [] represents a sandwich layer, write a recursive function count_layers() that returns
    the total number of sandwhich layers.

    Evaluate the time and space complexity of your solution. Define your variables and provide
    a rationale for why you believe your solution has the stated time and space complexity.
"""

def count_layers(sandwich: list):
    if len(sandwich) == 1:
        return 1
    
    next_layer = sandwich[1]

    return count_layers(next_layer) + 1

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = [
    "bread", [
        "cheese", [
            "ham", [
                "mustard", ["bread"]
                    ]
                ]
            ]
    ]

print(count_layers(sandwich1)) # expected output = 4
print(count_layers(sandwich2)) # expected output = 5