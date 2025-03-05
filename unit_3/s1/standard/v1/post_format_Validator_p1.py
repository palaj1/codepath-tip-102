"""
    Prompt:

    You are managing a social media platform and need to ensure that posts are properly formatted. Each 
    post must have balanced and correctly nested tags, such as:
     
        * () for mentions 
        * [] for hashtags  
        * {} for links

    You are given a string representing a post's content, and your task is to determine if the tags in the 
    post are correctly formatted.
    
    A post is considered valid if:
        
        1. Every opening tag has a corresponding closing tag of the same type.
        2. Tags are closed in the correct order. 
"""

def is_valid_post_format(posts: str):
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for c in posts:
        if c in bracket_map.values():
            stack.append(c)
        elif c in bracket_map:
            if not stack or stack.pop() != bracket_map[c]:
                return False

    return not stack

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))