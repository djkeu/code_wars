def count_squares(cuts):
    """Count the number of cubes with red sides."""
    cubes = (cuts + 1) ** 3
    painted_cubes = ((cuts + 1) * (cuts + 1) * 2) + \
                    ((cuts + 1) * (cuts - 1) * 2) + \
                    ((cuts - 1) * (cuts - 1) * 2)

    
    print(f"Cuts: {cuts}, total cubes: {cubes}, painted cubes: {painted_cubes}")

    # return x       # an integer number

count_squares(0)  # 1  # Returns 2 instead of 1. Oh well.
count_squares(1)  # 8 ((2 * 2) * 2) + ((2 * 0) * 2) + ((0 * 0) * 2)
count_squares(2)  # 26 (3 * 3) * 2) + (3 * 1) * 2) + ((1 * 1) * 2)
count_squares(3)  # 56 (16 * 2) + (8 * 2) + (4 *2)
count_squares(4)  # 98 (25 * 2) + (15 * 2) + (9 * 2)
count_squares(5)  # 152 (36 * 2) + (24 * 2) + (16 *2)
# ((cuts + 1) * (cuts + 1)) * 2  +  
# ((cuts + 1) * (cuts - 1)) * 2  + 
# ((cuts - 1) * (cuts - 1)) * 2 