integers = [ 5, 4, 3]


def pythagorean_triple(integers):
    """Check if a pythagorean triple can be made with three given integers."""
    integers = sorted(integers)
    
    a = integers[0]
    b = integers[1]
    c = integers[2]
    
    if a ** 2 + b ** 2 == c ** 2:
        print(True)
    else:
        print(False)

pythagorean_triple(integers)
