def is_it_letter(s):
    if s.isalpha():
        return True
    else:
        return False

def test_is_it_letter():
    assert is_it_letter('a') == True
    assert is_it_letter('A') == True
    assert is_it_letter('!') == False
    assert is_it_letter('1') == False


is_it_letter("a")


# https://www.codewars.com/kata/57a06b07cf1fa58b2b000252/train/python
