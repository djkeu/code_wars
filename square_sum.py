def square_sum(numbers):
    squared_numbers = []

    for number in numbers:
        number = number**2
        squared_numbers.append(number)
    return sum(squared_numbers)


def test_square_sum():
    assert square_sum([1,2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50
    assert square_sum([]) == 0
    assert square_sum([-1,-2]) == 5
    assert square_sum([-1,0,1]) == 2


square_sum(([1, 2, 4]))
# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
