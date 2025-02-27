"""
    Prompt:

    Given a string "pattern" and a string "schedule", return True if "schedule" follows the same pattern.
    Return False otherwise.

    Here, "follow" means a full match, such that there is a one-to-one correspondence between a letter in
    pattern and a non-empty word in schedule.

    You are provided with a partially implemented and buggy version of the solution. Identify and fix the 
    bugs in the code. Then, perform a thorough code review and suggest improvements.
"""

def schedule_pattern(pattern, schedule):
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))