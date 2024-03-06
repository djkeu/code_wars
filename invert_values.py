# Invert values

# My way, doesn't work with Codewars random tests
def invert(lst):
    """Invert all integers in a list."""
    for i in lst:
        n = lst.pop()
        if  n > 0:
            n = n - 2*n
        else:
            n = n + -2*n
        lst.insert(0, n)

    print(lst)
    return lst

invert([11,  22,  -33,  -44,  55])
invert([-1, -3, -5,  6,  2])


# Correct way
def invert_correctly(lst):
    print([-n for n in lst])
    return [-n for n in lst]

invert_correctly([111,  222,  333,  444, 555])
invert_correctly([-1, -3, -5, 6,  2])
