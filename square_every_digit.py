def square_digits(num):
    squared_numbers = []

    for digit in map(int, str(num)):
        squared_numbers.append(digit**2)
    print(squared_numbers)

    concatenated_number = ""
    for number in squared_numbers:
        concatenated_number += str(number)
    print(concatenated_number)

square_digits(9119)


def test_square_digits():
    assert square_digits(9119) == 811181
    assert square_digits(0) == 0


# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
