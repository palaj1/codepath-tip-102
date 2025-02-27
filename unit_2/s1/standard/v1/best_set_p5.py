"""
    Prompt:

    As part of the festival, attendees cast votes for their favorite set. Given a dictionary "votes" that
    maps attendees id numbers to the artist they voted for, return the artist that had the most number
    of votes. 
    
    If there is a tie, return any artist with the top number of votes.
"""

def best_set(votes: dict):
    chart = dict()

    for artist in votes.values():
        if artist in chart:
            chart[artist] += 1
        else:
            chart[artist] = 1
    
    max_votes = max(chart.values())
    
    for artist, count in chart.items():
        if count == max_votes:
            return artist

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))