import string


def is_pangram(s):
    for ch in list(string.ascii_lowercase):
        if ch not in list(s.lower()):
            return False

    return True


def test_pangram():        
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True


def test_not_pangram():        
    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False
    assert is_pangram("Aacdefghijklmnopqrstuvwxyz") == False
