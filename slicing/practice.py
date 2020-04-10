parrot = 'Norwegian Blue'
print(parrot[0 : 9])
# you can create a slice by producing 3 numbers
# separated by colons- start,stop and step
# A slice starts from the first digit upto but not
# including the second digit
print(parrot[:9])
# the start point defaults to zero
print(parrot[0:])
#the stop point defaults to the end
print(parrot[-4:-2])#slicing with negative numbers
print(parrot[-4:12])
print(parrot[-2:12])
#no output
print(parrot[0:6:2])#using a step in a slice
print(parrot[0:6:4])
number = "9,223;372:036,854,775;807"
print(number[1::4])
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else "" for char in number).split()
print([int(val) for val in values])
