def validate_pin(pin):
    #return true or false
    pass


def test_validate_pin():    
    test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
    test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
    test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
    test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
    test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
    test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
    test.assert_equals(validate_pin("-12345"),False, "Wrong output for '-12345'")
    test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
    test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")



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
