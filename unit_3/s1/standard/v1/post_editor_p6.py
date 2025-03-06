"""
    Prompt:
    
    You want to add a creative twist to your posts by reversing the order of characters in each word within 
    your post while still preserving whitespace and the initial word order.

    Given a string post, use a queue to reverse the order of characters in each word within the sentence
"""

# I'm surprised that queue was considered for this, it doesn't make sense because it preserves the order
# meaning that we would have to treat the queue as a stack, retreiving from the back of the queue not front
def edit_post(post):
    words = post.split(" ")
    result = []

    for word in words:
# Preferred to use a list as the queue for simplicity, but am aware of the disadvantages
        queue = []
        
        for i in range(len(word) - 1, -1, -1):
            queue.append(word[i])

        reversed_word = "".join(queue.pop(0) for _ in range(len(queue)))
        result.append(reversed_word)

    return " ".join(result)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))
