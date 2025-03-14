"""
    Prompt:
     
    You want to provide an overview of the NFT collection to potential buyers. One key statistic is the 
    average value of the NFTs in the collection. However, if the collection is empty, the average value 
    should be reported as 0.

    Write the average_nft_value function, which calculates and returns the average value of NFTs in the 
    collection.

    Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
    for why you believe your solution has the stated time and space complexity.
"""

# Time complexity O(n) and space complexity of O(1)
#   * TC - needs to parse nft_collection when using list comprehension inside the sum() function
#   * SC - doesn't use extra space
def average_nft_value(nft_collection):
    if not nft_collection: 
        return 0
    
    return sum(entry["value"] for entry in nft_collection) / len(nft_collection)
    

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection)) # -> 5.7

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))  # -> 9.15

nft_collection_3 = []
print(average_nft_value(nft_collection_3))  # -> 0