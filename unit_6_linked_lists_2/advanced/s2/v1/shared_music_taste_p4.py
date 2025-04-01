"""
    Prompt:

    Given the heads of two singly linked lists playlist_a and playlist_b, return the node at
    which the two lists intersect. If the two lists have no interseciton at all. return None.

    There are no cycles anywhere in either linked list. The linked lists must retain their 
    original structure after the function returns. 

    Evaluate the time and space complexity of your solution. Define your variables and provide 
    a rationale for why you believe your solution has the states time and space complexity. 
"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def playlist_overlap(playlist_a: Node, playlist_b: Node):
    # Without a next node to compare we can't reach an intersection
    if not playlist_a or not playlist_b:
        return None

    ptr_a, ptr_b  = playlist_b, playlist_a

    # while we haven't reached the end, assign both pointers accordingly
    while ptr_a != ptr_b:
        ptr_a = ptr_a.next if ptr_a else playlist_b        
        ptr_b = ptr_b.next if ptr_b else playlist_a        

    return ptr_a


playlist_a = Node('Song A', Node('Song B'))
playlist_b = Node('Song X', Node('Song Y', Node('Song Z')))
shared_segment = Node('Song M', Node('Song N', Node('Song O')))

playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment

print((playlist_overlap(playlist_a, playlist_b)).value)

