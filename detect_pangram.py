import string


def is_pangram(s):
    list_alphabet = list(string.ascii_lowercase)
    list_string = list(s.lower())
    #print(list_alphabet)
    #print(list_string)

    for ch in list_alphabet:
        if ch not in list_string:
            return False
        else:
            return True

is_pangram("Hallo")
is_pangram("bcdefghijklmnopqrstuvwxyz")


def test_pangram():        
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True


def test_not_pangram():        
    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False
    assert is_pangram("Aacdefghijklmnopqrstuvwxyz") == False
