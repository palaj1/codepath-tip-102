"""
    Prompt:

    You are working as an engineer normalizing volume levels on songs. Given the head of a 
    singly linked list with integer values 'song_audio' representing volume levels at different
    points in a song, return the number of critical points. A critical point is a local minima
    or maxima.

        * The head and tail nodes are not considered critical points.
        * A node is a local minima if both the next and previous elements are greater than 
          the current element
        * A node is a local maxima if both the next and previous elements are less than the 
          current element
    
    Evaluate the time and space complexity of your solution. Define your variables and provide
    a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
    if not song_audio or not song_audio.next:
        return 0
    
    # We need a way to have reference the previous node's value
    previous_node = song_audio

    # The first node shouldn't be the start of our condition, it should be the second node
    current_node = song_audio.next

    maxima_minima_counter = 0

    while current_node.next:
        # Checking for minima case
        if current_node.value < previous_node.value and current_node.value < current_node.next.value:
            maxima_minima_counter += 1

        # Checking for maxima case
        if current_node.value > previous_node.value and current_node.value > current_node.next.value:
            maxima_minima_counter += 1  

        previous_node = current_node
        current_node = current_node.next

    return maxima_minima_counter

# contains 1 minima and 2 maxima
song_audio = Node(5, 
                  Node(3, 
                       Node(1, 
                            Node(2, 
                                 Node(5, 
                                      Node(1, Node(2))
                                    )
                                )
                            )
                        )
                    )

# contains 1 minima and 3 maxima
song_audio2 = Node(5, 
                   Node(3, 
                        Node(1, 
                             Node(2, 
                                  Node(5, 
                                       Node(1, 
                                            Node(2, Node(0))
                                        )
                                    )
                                )
                            )
                        )
                    )

print(count_critical_points(song_audio))
print(count_critical_points(song_audio2))