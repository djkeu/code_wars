def subtract_sum(number):

    #1: Ask for input of a number >= 10 and < 10_000
    number = input("Enter a number between 10 and 10000: ")
    number = int(number)

    if number < 10:
        print("Enter a larger number please.")
    elif number >= 10_000:
        print("Enter a smaller number please.")
    else:
        sum = 0

        for digit in str(number):
            sum += int(digit)

        number = number - sum

    print(f"The fruit is {number}")

    kiwis = [24, 26, 47, 49, 68, 70, 91, 93]
    pears = [21, 23, 42, 44, 46, 65, 67, 69, 88]
    bananas = [25, 27, 29, 48, 50, 71, 73, 92, 94, 96]
    melons = [28, 30, 32, 51, 53, 74, 76, 95, 97]
    pineapples = [10, 12, 31, 33, 52, 56, 75, 77, 79, 98, 100]
    apples = [918, 27, 36, 45, 54, 63, 72, 81, 90, 99]
    cucumbers = [11, 13, 34, 57, 59, 78, 80]
    oranges = [14, 16, 35, 37, 39, 58, 60, 83]
    grapes = [15, 17, 19, 38, 40, 61, 82, 84, 86]
    cherries = [20, 22, 41, 43, 62, 64, 66, 85, 87, 89]

    if number in kiwis:
        fruit = "kiwi"
    elif number in pears:
        fruit = "pear"
    elif number in bananas:
        fruit = "banana"
    elif number in melons:
        fruit = "melon"
    elif number in pineapples:
        fruit = "pineapple"
    elif number in apples:
        fruit = "apple"
    elif number in cucumbers:
        fruit = "cucumber"
    elif number in oranges:
        fruit = "orange"
    elif number in grapes:
        fruit = "grape"
    elif number in cherries:
        fruit = "cherry"
    else:
        fruit = "apple"

    print(fruit)

    # return #fruit name like "apple"

subtract_sum(4)

