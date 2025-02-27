"""
    Prompt:

    Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she
    can trust the message if it contains all of the letters int he alphabet/ Given a string message 
    containing only lowercase English letters and whitespace, write a function can_trust_message() that
    returns True if the message contains every letter of the English alphabet at least once, and False
    otherwise.
"""

def can_trust_message(message: str):
    pointer = 97

    raw_text = message.replace(" ", "").lower()
    sorted_text = sorted(raw_text)

    for c in sorted_text:
        if ord(c) == pointer:
            pointer += 1

        if pointer > 122:
            break
    
    return pointer == 123


message1 = "sphinx of blaack quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))