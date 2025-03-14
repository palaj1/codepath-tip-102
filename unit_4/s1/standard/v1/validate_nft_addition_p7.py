"""
    Prompt: 
    
    You want to ensure that NFTs are added in a balanced way. For example, every "add" action must be 
    properly closed by a corresponding "remove" action.

    Write the validate_nft_actions() function, which takes a list of actions (either "add" or "remove") 
    and returns True if the actions are balanced, and False otherwise.

    A sequence of actions is considered balanced if every "add" has a corresponding "remove" and no "remove"
    occurs before an "add".

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
    for why you believe your solution has the stated time and space complexity.
"""

# Time complexity O(n) and space complexity O(n)
#   * TC - parses the passed in parameter list of "actions", where it contains "n" elements 
#   * SC - uses a stack list where it is populated "n" times in a worst case scenario
def validate_nft_actions(actions):
    stack = []

    for action in actions:
        if action == "add":
            stack.append(action)
        elif action == "remove":
            if stack and stack[-1] == "add":
                stack.pop()
            else:
                return False
        else:
            return False
        
    return True


actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions)) # -> True
print(validate_nft_actions(actions_2)) # -> True
print(validate_nft_actions(actions_3)) # -> False


# Extra
actions_4 = ["add", "remove", "add", "remove", "remove"]
print(validate_nft_actions(actions_4)) # -> False