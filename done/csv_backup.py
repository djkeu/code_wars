def to_csv_text(array):
    """Return the CSV representation of a two-diminsional array."""

    csv_string = "'" 
        

    for inner in array:

        # First inner array
        if inner == array[0]:

            # FIXME: Only the integers need to be converted, not the list.
            # Worked around it by stripping the abundant characters before return.
            csv_string = csv_string.join(str(inner))#.join(", ")  

            """
            for item in inner:
                if item != inner[-1]:
                    print(f"{item},", end='')
                elif item == inner[-1]:
                    print(f"{item}", end='')

            print("\\n'")
            """
            csv_string += "\\n"

        # Middle inner arrays
        elif inner != array[-1]:
            print("+'", end='')

            for item in inner:
                if item != inner[-1]:
                    print(f"{item},", end='')
                elif item == inner[-1]:
                    print(f"{item}", end='')

            print("\\n'")

        # Last inner array
        elif inner == array[-1]:
            print("+'", end='')

            for item in inner:
                if item != inner[-1]:
                    print(f"{item},", end='')
                elif item == inner[-1]:
                    print(f"{item}", end='')

            print("'")
            
    csv_string = csv_string.replace('[', '').replace("'", "")
    csv_string = csv_string.replace(" ", "").replace("]", "")

    print(f"\nDe CSV string: {csv_string}\n")
    return csv_string




input =  [[ 0, 1, 2, 3, 4 ],
            [ 10,11,12,13,14 ],
            [ 20,21,22,23,24 ],
            [ 30,31,32,33,34 ]]

to_csv_text(input)






"""
input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 
    
output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
"""
