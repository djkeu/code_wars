import re


def validate_pin(pin):
    if re.fullmatch("^\\d{4}$", pin) or re.fullmatch("^\\d{6}$", pin):
        return True
    else:
        return False


def test_validate_corect_pin():
    assert validate_pin("1234") == True
    assert validate_pin("0000") == True
    assert validate_pin("1111") == True
    assert validate_pin("123456") == True
    assert validate_pin("098765") == True
    assert validate_pin("000000") == True
    assert validate_pin("123456") == True
    assert validate_pin("090909") == True


def test_validate_incorect_pin():    
    assert validate_pin("1") == False
    assert validate_pin("12") == False
    assert validate_pin("123") == False
    assert validate_pin("12345") == False
    assert validate_pin("1234567") == False
    assert validate_pin("-1234") == False
    assert validate_pin("-12345") == False
    assert validate_pin("1.234") == False
    assert validate_pin("00000000") == False


# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
