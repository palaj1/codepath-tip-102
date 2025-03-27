"""
    Prompt:

    A variation of the two-pointer technique introduced in previous units is to have a slow 
    and fast pointer that increment at different rates.

    We would like to check whether our plylist loops or not. Given the head of a linked list 
    'playlist_head', return 'True' if the playlist has a cycle in it and 'False' otherwise.
    A linked list has a cycle if at some point int he list, the node's next pointer points back
    to a previuos node in the list.

    Evaluate the time and space complexity of your solution. Define your variables and provide
    a rationale for why you believe your solution has the stated time and space complexity.
    
"""

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    if not playlist_head:
        return False
    
    slow = playlist_head
    fast = playlist_head.next

    # When no cycle exists, the fast pointer will reach the end
    while fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next
    
    return False


song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4

print(on_repeat(song1))