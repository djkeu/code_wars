# list_of_mulitples.py

def find_multiples(integer, limit):
    """Return list of multiples of an integer up to limit."""
    list_of_multiples = []
    i = integer

    while integer <= limit:
        list_of_multiples.append(integer)
        integer += i

    print(list_of_multiples)
    return list_of_multiples

find_multiples(2, 8)
find_multiples(3, 17)