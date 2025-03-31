"""
    Prompt:

    You are given the head of two linked lists, playlist1, and playlist2 with lengths n and m respectively. 

    Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place. 

    Assume the lists are 0-indexed.
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

def merge_playlists(playlist1, playlist2, a, b):
    if not playlist1:
         return playlist2
    
    if not playlist2:
         return playlist1

    dummy = Node(None, playlist1)
    prev = dummy

    for _ in range(a):
        if not prev.next:
            break
        prev = prev.next 

    current = prev.next
    for _ in range(b - a):
        if not current:
            break

        current = current.next
    
    node_after_b = current.next if current else None

    prev.next = playlist2

    tail_playlist2 = playlist2
    while tail_playlist2.next:
         tail_playlist2 = tail_playlist2.next
    
    tail_playlist2.next = node_after_b

    return dummy.next
         
playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

# ============================== General Input ==============================
# ('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant') -> ('Empty', 'Kevin Abstract')

# Expected output:
# ('Flea', 'St.Vincent') -> ('Juice', 'Lizzo')  -> ('First', 'Gallant') -> ('Empty', 'Kevin Abstract')
print_linked_list(merge_playlists(playlist1, playlist2, 2, 2))

# Expected output:
# ('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant')
# print_linked_list(merge_playlists(playlist1, playlist2, 4, 4))

# Expected output:
# ('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant') -> ('Empty', 'Kevin Abstract')
# print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
