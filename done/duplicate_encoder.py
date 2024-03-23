def duplicate_encode(word):
    encoded_word = ""

    for c in word.lower():
        if word.lower().count(c) == 1:
            encoded_word += "("
        else:
            encoded_word += ")"
    
    return encoded_word


def test_duplicate_encode():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"  # "should ignore case"
    assert duplicate_encode("(( @") == "))(("


# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
