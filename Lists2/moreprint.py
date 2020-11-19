name = 'Tim'
age = 10

print(name,age,'Python',2020) # *args
print(name, age, 'Python', 2020, sep=', ') #separator (keyword argument)
                                           #if no argument is provided sep defaults
                                           #to a space.
                                           #used when we pass more than one value
                                           #to the print function.

print((name,age,'Python',2020)) #tuple #one object
