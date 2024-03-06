import sys

def total_bytes(object):
    """Return the total of bytes an object takes in memory."""
    return sys.getsizeof(object)

test = total_bytes([4, 7])
print(test)
