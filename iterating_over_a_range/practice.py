for i in range(1, 20):
    print("i is now {0}".format(i))
#the last value specified in ranges is not included
#range produces a range of values from the starting
#value upto but not including the end value
for i in range(10): #starting point defaults to zero
    print(i)
# Python range() function returns an immutable sequence 
# object of integers, so it is possible to convert the 
# output of a range() to the Python list.
for number in range(0 , 100 , 7):
    print(number)

#range() is a built-in function of Python. It is used when a user needs to perform an action for 
#a specific number of times.
8