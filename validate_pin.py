import re


def validate_pin(pin):
    if re.search("^\\d{4}$", pin) or re.search("^\\d{6}$", pin):
        return True
    else:
        return False
   


def test_validate_corect_pin():    
    assert validate_pin("1234") == True
    assert validate_pin("123456") == True


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



"""
Description:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""


# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
