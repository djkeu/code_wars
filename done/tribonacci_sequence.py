def tribonacci(signature, n):
    tribo_list = []
    
    if n == 0:
        return tribo_list
    elif n == 1:
        tribo_list.append(signature[0])
        return tribo_list
    elif n == 2:
        tribo_list.append(signature[0])
        tribo_list.append(signature[1])
        return tribo_list
    
    for number in signature:
        tribo_list.append(number)

    i = 0
    while i < n-3:
        tribo_list.append(tribo_list[i] + tribo_list[i+1] + tribo_list[i+2])    
        i += 1
    
    return tribo_list


def test_tribonacci():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
    assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
    assert tribonacci([1, 1, 1], 1) == [1]
    assert tribonacci([300, 200, 100], 0) == []
    assert tribonacci([0.5, 0.5, 0.5], 30) == [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]


# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
