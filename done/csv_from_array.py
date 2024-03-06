def to_csv_text(array):
    """Return the CSV representation of a two-diminsional array."""
    csv_string = "" 

    for inner in array:
        if inner != array[-1]:
            middle_string = str(inner)
            middle_string += "\\n"
            csv_string += middle_string

        elif inner == array[-1]:
            last_string = str(inner)
            csv_string += last_string
            
    csv_string = csv_string.replace('[', '').replace("'", "")
    csv_string = csv_string.replace(" ", "").replace("]", "")

    return csv_string


input =  [[ 0, 1, 2, 3, 4 ],
            [ 10,11,12,13,14 ],
            [ 20,21,22,23,24 ],
            [ 30,31,32,33,34 ]]

test = to_csv_text(input)
print(f"CSV string: {test}")

