def duplicate_encode(word):
    word = word.lower()

    encoded_word = ""
    for c in word:
        if word.count(c) == 1:
            encoded_word += "("
        else:
            encoded_word += ")"
    
    return encoded_word

    # ToDo: list comprehension


def test_duplicate_encode():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"  #"should ignore case"
    assert duplicate_encode("(( @") == "))(("


"""
Instructions:
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

"""


# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
