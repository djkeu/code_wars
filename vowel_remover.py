my_string = 'hello'
lowercase_vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in lowercase_vowels:
    result_string = my_string.replace(vowel, '')
    my_string = result_string
    
print("My string:")
print(my_string)


# Without the list of lowercase vowels
second_string = 'hallo allemaal'
for vowel in 'aeiou':
    result_string = second_string.replace(vowel, '')
    second_string = result_string

print("Second string:")
print(second_string)

