# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    print(f"Original list: {lst}")
    for n in lst:
        if n == 0:
            lst.append(lst.pop(lst.index(n)))

    print(f"Altered list: {lst}")
    return lst

move_zeros([1, 0, 1, 2, 0, 1, 3])
print(f"Expected list: [1, 1, 2, 1, 3, 0, 0]")