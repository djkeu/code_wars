def replace_exclamation(st):
    return st


def test_replace_exclamation():
    assert replace_exclamation("Hi!") == "H!!"
    assert replace_exclamation("!Hi! Hi!") == "!H!! H!!"
    assert replace_exclamation("aeiou") == "!!!!!"
    assert replace_exclamation("ABCDE") == "!BCD!"


# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python
