"""
    Prompt:

    You are given the head of a singly linked list playlist. 
    
    The list can be represented as:
        L0 -> L1 -> ... -> Ln - 1 -> Ln
    
    Shuffle the playlist to have the following form:
        L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2-> ...

    You may not modify the values in the list's nodes. Only the order of the nodes 
    themselves may be changed. 
    
    Return the head of the shuffled list.

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
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def split_list(head: Node):
    if not head:
        return None, None
    
    # slow fast methodm retrieving having access to node before the actual middle node
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    return head, second_half

def reverse_list(head: Node):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def shuffle_playlist(playlist: Node):
    if not playlist or not playlist.next:
        return playlist
    
    # FInd middle node, will allow us to create the structure
    first_half, second_half = split_list(playlist)

    # Reverse the second half
    reversed_second_half = reverse_list(second_half)

    # dummy node for the sole purpose of having direct access to the head (entire linked list)
    dummy = Node(None)

    # tail node to build the linked list
    tail = dummy


    while first_half or reversed_second_half:
        # add current first_half head to tail, reassign tail
        if first_half:
            tail.next = first_half
            first_half = first_half.next
            tail = tail.next
        
        # add current reversed_second_half head to tail, reassign tail
        if reversed_second_half:
            tail.next = reversed_second_half
            reversed_second_half = reversed_second_half.next
            tail = tail.next

    # return the head of the linked list
    return dummy.next        


playlist1 = Node(1, 
                Node(2, 
                    Node(3, 
                         Node(4, Node(6))
                        )
                    )
                )

playlist2 = Node(('Respect', 'Aretha Franklin'),
                Node(('Superstition', 'Stevie Wonder'),
                    Node(('Wonderwall', 'Oasis'),
                        Node(('Like a Prayer', 'Madonna'),
                            Node(('Bohemian Rhapsody', 'Queen'))))))

# Expected Output:
#  1 -> 6 -> 2 -> 4 -> 3
print_linked_list(shuffle_playlist(playlist1))

# Expected output:
# ('Respect', 'Aretha Franklin') -> ('Bohemian Rhapsody', 'Queen') -> ('Superstition', 'Stevie Wonder') ->
# ('Like a Prayer', 'Madonna') -> ('Wonderwall', 'Oasis')
print_linked_list(shuffle_playlist(playlist2))