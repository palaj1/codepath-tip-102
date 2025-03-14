"""
    Prompt:

    NFTs are added to a processing queue before they are displayed. The queue processes NFTs in a First-In,
    First-Out (FIFO) manner. Each NFT has a processing time, and you need to determine the order in which 
    NFTs should be processed based on their intial position in the queue.

    Write the process_nft_queue() function, which takes a list of NFTs. The function should return a list of
    NFT names in the order they were processed.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
    for why you believe your solution has the stated time and space complexity.
"""
from collections import deque

# I noticed I understood the problem incorrectly, it only wants a list ordered based on entry's intial 
# position, but I also noticed I'm technically processing in a Round-robin manner, which is something
# explored in OS (cool) 

# Time complexity O(n) and space complexity O(n)
#   * TC - enqueues and dequeues entire queue until empty, queue has "n" elements
#   * SC - uses a deque and an output list which take "n" elements each
def process_nft_queue(nft_queue): 
    queue = deque((entry["name"], entry["processing_time"]) for entry in nft_queue)

    order = []

    while queue:
        process = queue.popleft()

        if process[1] > 1:
            queue.append((process[0], process[1] - 1))
        else:
            order.append(process[0])

    return order

# Time complexity O(n) and space complexity O(n)
#   * TC - only enqueues entries and then parses them until queue is empty, queue has "n" elements 
#   * SC - uses a deque and an output list which take "n" elements each
def process_nft_queue(nft_queue):
    queue = deque(nft_queue)
    order = []

    while queue:
        nft = queue.popleft()
        order.append(nft["name"])

    return order

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue)) # -> ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2)) # -> ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3)) # -? ['Crypto Kitty', 'Galactic Voyage']