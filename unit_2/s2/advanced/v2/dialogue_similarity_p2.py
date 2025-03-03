"""
    Prompt:

    Watching a reality TV show, you notice a lot of contestants talk similarly. We want to determine if
    two contestants have similar speech patterns.

    We can represent a sentence as an array of words, for example, the sentence "I've got a text!" can be 
    represented as sentence = ["I've", "got", "a", "text"]

    You are given two sentences from different contestants sentence1 and sentence2 each represented as a 
    string array and given an array of string pairs similar_pairs where similar_pairs[i] = [xi, y1] 
    indicates that the two words x1 and y1 are similar. 

    Write a function is_similar() that returns True if sentence1 and sentence2 are similar, and False if
    they are not similar.
        
        * They have the same length (i.e., the same number of words)
        * sentence1[i] and sentence2[i] are similar
    
    Notice that a word is always similar to itself, also notice that the similarity relation is not 
    transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c
    are not necessarily similar.
"""

def is_similar(sentence1: str, sentence2: str, similar_pairs: list):
    if len(sentence1) != len(sentence2):
        return False

    similarity_dict = dict()

    for w1, w2 in similar_pairs:
        if w1 not in similarity_dict:
            similarity_dict[w1] = set()
        if w2 not in similarity_dict:
            similarity_dict[w2] = set()
        
        similarity_dict[w1].add(w2)
        similarity_dict[w2].add(w1)

    for word in set(sentence1) | set(sentence2):
        if word not in similarity_dict:
            similarity_dict[word] = set()
        similarity_dict[word].add(word)
    
    return all(w2 in similarity_dict[w1] for w1, w2, in zip(sentence1, sentence2))




sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))