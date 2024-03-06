def grow(arr):
    result = 1

    for i in arr:
        result *= i

    return result

test = grow([3, 7, 2])
print(test)
