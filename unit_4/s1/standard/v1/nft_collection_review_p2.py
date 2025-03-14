"""
    Prompt: 

    You're responsible for ensuring quality of the NFT collection before it is displayed in the virtual 
    gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the
    collection. A junior developer wrote the intial version of this function, but it contains some bugs
    that prevent it from working correctly

    Task:
        1. Review the provided code and identify the bug(s)
        2. Explain what the bug is and how it affects the output
        3. Refactor the code to fix the bug(s) and provide the correct implementation
"""

def extract_nft_names(nft_collection):
    nft_names = []

    for nft in nft_collection:
        # Incorrect list population below
        # nft_names += nft["names"]

        # Correct list population below
        nft_names.append(nft["name"])

    return nft_names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []


print(extract_nft_names(nft_collection)) # -> ['Abstract Horizon', 'Pixel Dreams']
print(extract_nft_names(nft_collection_2)) # -> ['Golden Hour']
print(extract_nft_names(nft_collection_3)) # -> []
