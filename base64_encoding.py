# https://www.codewars.com/kata/5270f22f862516c686000161/train/python

"""
Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.

You can learn more about Base64 encoding and decoding here:
http://en.wikipedia.org/wiki/Base64

Note: This kata uses the non-padding version ("=" is not added to the end).
"""

"""
'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'
"""

def to_base_64(string):
    pass
    #your code here
    
def from_base_64(string):
    pass
    #your code here



# Tests
"""
vfrom solution import to_base_64, from_base_64
import codewars_test as test

@test.describe("Basic tests")
def _():
    @test.it("Tests")
    def __():
        cases = [["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
          ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
          ["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
          ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
          ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
          ["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
          ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
          ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
          ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]]

        for x, y in cases:
            result=to_base_64(x)
            test.assert_equals(result, y)
            test.assert_equals(from_base_64(result), x)
"""