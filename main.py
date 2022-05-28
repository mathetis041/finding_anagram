# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    """
    find all anagrams of a word in a list of words.
    """
    word = word.lower()
    anagram = anagram.lower()
    
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")
    
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False


print(find_anagram("hello", "check"))
print(find_anagram("elbow", "below"))  


