def is_palindrome(s):
    """Check if a string is a palindrome"""
    s = s.lower()
    reverse_s = s[::-1]
    
    if reverse_s == s:
        return True
    else:
        return False

"""
Prefered solution from Codewars
s = s.lower()
    return s == s[::-1]
"""

test_string_1 = is_palindrome("Marc Kooij")
print(test_string_1)

test_string_2 = is_palindrome("aha")
print(test_string_2)

test_string_3 = is_palindrome("12321")
print(test_string_3)

