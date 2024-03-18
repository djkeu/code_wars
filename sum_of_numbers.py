def get_sum(a,b):
    if a == b:
        return a
    elif b > a:
        arr = list(range(a, b+1))
    else:
        arr = list(range(b, a+1))

    sum = 0
    for n in arr:
        sum += n
    return sum


def test_get_sum():
    assert get_sum(0, 1) == 1
    assert get_sum(0,-1) == -1
    assert get_sum(1, 0) == 1  # (1 + 0 = 1)
    assert get_sum(1, 2) == 3  # (1 + 2 = 3)
    assert get_sum(0, 1) == 1  # (0 + 1 = 1)
    assert get_sum(1, 1) == 1  # (1 since both are same)
    assert get_sum(-1, 0) == -1  # (-1 + 0 = -1)
    assert get_sum(-1, 2) == 2  # (-1 + 0 + 1 + 2 = 2)


# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
