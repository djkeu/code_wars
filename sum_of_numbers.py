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


def test_get_sum_a_equals_b():
    assert get_sum(1, 1) == 1
    assert get_sum(12, 12) == 12
    assert get_sum(-1, -1) == -1
    assert get_sum(-12, -12) == -12
    assert get_sum(0, 0) == 0


def test_get_sum_b_larger_than_a():
    assert get_sum(0, 1) == 1       # (0 = 1 = 1)
    assert get_sum(1, 3) == 6       # (1 + 2 + 3 = 6)
    assert get_sum(-1, 0) == -1     # (-1 + 0 = -1)
    assert get_sum(-1, 2) == 2      # (-1 + 0 + 1 + 2 = 2)


def test_get_sum_a_larger_than_b():
    assert get_sum(1, 0) == 1       # (1 + 0 = 1)
    assert get_sum(2, 1) == 3       # (0 + -1 = -1)
    assert get_sum(0,-1) == -1      # (0 + -1 = -1)
    assert get_sum(2, -1) == 2      # (1 + 0 = 1)


# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
