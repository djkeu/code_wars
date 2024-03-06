# https://flexiple.com/python/python-append-to-string/

first_name = "Emma"
second_name = "Watson"

print ("The first name: " + str(first_name))
print ("The second name: " + str(second_name))

list = [first_name, second_name]
string = "".join(list)

print ("The appended string: " + string)

