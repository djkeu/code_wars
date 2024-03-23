def get_count(sentence):
    pass

`
def all_vowels():
    assert get_count("aeiou") == 5, f"Incorrect answer for \"aeiou\""
    

def only_y():
    assert get_count("y") == 0, f"Incorrect answer for \"y\""
    

def no_vowels():
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\""
    

def no_vowels():
    assert get_count("") == 0, f"Incorrect answer for empty string"
    

def test_abracadabra():    
    assert get_count("abracadabra") == 5, f"Incorrect answer for \"abracadabra\""


"""
Instructions:
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""


# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
