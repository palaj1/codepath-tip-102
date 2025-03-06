"""
    Prompt:

    On your platform, comments on posts are displayed in the order they are received. However, for a 
    special feature, you need to reverse the order of comments before displaying them. Given a queue of
    comments represented as a list of strings, reverse the order using a stack
"""

def reverse_comments_queue(comments):
    return [comments.pop() for i in range(len(comments))]


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))