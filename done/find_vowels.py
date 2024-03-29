def vowel_indices(word):
    word = word.lower()
    found_vowels = []
    
    for i, ch in enumerate(word.lower()):
        if ch in list("aeiouy"):
            found_vowels.append(i+1)

    return found_vowels


def test_vowel_indices():
    assert vowel_indices("mmm") == []
    assert vowel_indices("apple") == [1,5]
    assert vowel_indices("123456") == []
    assert vowel_indices("UNDISARMED") == [1,4,6,9]
    assert vowel_indices("supercalifragilisticexpialidocious") == [2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 25, 27, 29, 31, 32, 33]
    assert vowel_indices("Implied") == [1, 5, 6]
    

"""
Instructions:
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]

NOTES

    Vowels in this context refers to: a e i o u y (including upper case)
    This is indexed from [1..n] (not zero indexed!)
"""

# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
