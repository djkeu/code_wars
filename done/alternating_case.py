def to_alternating_case(string):
    """Switch upper- and lowercase characters of a string."""
    #return string.swapcase()  # Builtin method swapcase()

    list_from_string = [i for i in string]

    for char in list_from_string:
        char = list_from_string.pop()

        if char.islower():
            list_from_string.insert(0, char.upper())
        else:
            list_from_string.insert(0, char.lower())

    return ''.join(list_from_string)
    

test = to_alternating_case("Marc Kooij")
print(test)
