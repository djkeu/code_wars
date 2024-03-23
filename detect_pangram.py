import string


def is_pangram(s):
    list_alphabet = list(string.ascii_lowercase)

    for ch in list_alphabet:
        if ch not in list(s):
            return False
        else:
            return True


def test_pangram():        
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True


def test_not_pangram():        
    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False
