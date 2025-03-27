"""
    Prompt:

    Given the head of a linked list 'playlist_head' that may contain a cycle, use the fast and
    slow pointer method to return the length of the cycle. If the list does not contain a cycle,
    return 0.

    Evaluate the time and space complexity of your solutioon. Define your variables and provide
    a rationale for why you believe your solution has the stated time and space complexity
"""
class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    if not playlist_head:
        return 0
    
    slow = playlist_head
    fast = playlist_head.next
    counter = 0

    while fast and fast.next:
        if slow == fast:
            return counter + 1
        
        counter += 1
        slow = slow.next
        fast = fast.next.next
    
    return 0
        

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

# function call with cycle
print(loop_length(song1))

song4.next = None

# function call without cycle
print(loop_length(song1))
