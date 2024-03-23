def get_count(sentence):
    vowels = list("aeiou")
    vowel_count = 0

    for c in sentence:
        if c in vowels:
            vowel_count +=1

    return vowel_count


def test_all_vowels():
    assert get_count("aeiou") == 5
    

def test_only_y():
    assert get_count("y") == 0
    

def test_no_vowels():
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    

def test_no_vowels():
    assert get_count("") == 0
    

def test_abracadabra():    
    assert get_count("abracadabra") == 5


"""
Instructions:
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""


# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
