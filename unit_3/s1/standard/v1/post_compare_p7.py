"""
    Prompt:

    You often draft your posts and edit them before publishing. 

    Given two draft strings draft1 and draft2, return True, if they are equal when both are typed into
    empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will remain empty
"""

def remove_backspaces(s):
    stack = []

    for c in s:
        if stack and c == "#" :
            stack.pop()
        else:
            stack.append(c)
    
    return "".join(stack)

def post_compare(draft1, draft2):
    return remove_backspaces(draft1) == remove_backspaces(draft2)
    

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 