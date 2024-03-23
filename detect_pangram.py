def is_pangram(s):
    return False


def test_pangram():        
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True


def test_not_pangram():        
    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False
