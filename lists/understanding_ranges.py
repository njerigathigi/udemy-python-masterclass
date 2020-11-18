# print(range(100))
# #shows you how to get a range object with a start of 0 and a stop of 100.
# my_list = list(range(10))
# print(my_list)

# for value in range(1 ,10 ,2):
#     print(value)

# A step is an optional argument of a range() . 
# The step is a difference between each number in the result sequence.
# If the step size is 2, then the difference between each number is 2. 
# The default size of a step is 1 if not specified
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))

# print(even)
# print(odd)

# range(10)   #these two will use the same amount of memory
# range(1000000)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index("e")) 
# #Searches the string for a specified value 
# # and returns the position of where it was found
# print(my_string[4])
# small_decimals = range(0 ,10)
# print(small_decimals)
# print(small_decimals.index(3))

# odd = range(1, 10000 ,2)
# print(odd)

# print(odd[985])

# sevens = range(7 , 1000000, 7)
# x = int(input("please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by 7".format(x))

# # print(small_decimals)

# # my_range = small_decimals[::2]
# # print(my_range)
# # print(my_range.index(4))

# decimals = range(0 ,100)
# my_range = decimals[3:40:3]
# print(my_range)
# for i in my_range:
#     print(i)

# print ('=' * 40)

# for i in range(3, 40, 3):
#     print(i)

# print(my_range == range(3, 40, 3)) #True #test for equality
# print(range(0, 5, 2) == range(0, 6, 2)) #True

# r = range(0 , 100)
# print(r)

# for i in r[::-2]: #Negative indexing means beginning from the end, 
#                   #-1 refers to the last item, -2 refers to the second last item 
#                   #etc. The beginning and end values are reversed.
#     print(i)
# print('=' * 50)
# # :-2] == range(99, 0, -print(range(0, 100)[:2))
# for i in range(0, 100 , -2): #starts at 0 and moves back in steps of 2.
                             #hence no output.
    # print(i)
# backstring = ".egaugnal lufrewop yrav a si nohtyp"
# print(backstring[::-1])

# r = range(0 ,10)
# for i in r[::-1]:
#     print(i)

#Experiment with diff ranges and slices to get a feel for how they work.
#remember that you can print the range as well as iterating through it
#to print its values, to check that your ranges are what you expected.
#you may also want to include things like:
o = range(0 , 100, 4)
print(0)
# for i in o:
#     print(i)
p = o[::5] # expect 0 , 5 , 10 ,15 etc
print(p)
for i in p:
    print(i)

#and see if you can work out what will be printed before running the program.
#if you are unsure, use a for loop to print out the values of o to see why p
#returns what it does.
