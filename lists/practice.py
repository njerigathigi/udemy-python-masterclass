# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))
# parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
# parrot_list.append("A Norwegian Blue")
# for state in parrot_list:
#     print("This parrot is " + state)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# # numbers.sort() #works on the existing object.Does not create a new one.
# # print(sorted(numbers)) #This inbuilt function returns a new object.
# numbers_in_order = sorted(numbers)

# if numbers == numbers_in_order:
#     print("The lists are equal.")
# else:
#     print("The lists are not equal")
# #lists are not equal
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")

# list_1 = []
# list_2 = list() #list constructor. can be called with a single iterable parameter.

# print("list 1: {}".format(list_1))
# print("list 2: {}".format(list_2))

# if list_1 == list_2:
#     print("The lists are equal")
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
# # another_even = even
# another_even = list(even)
# print(another_even is even)
# another_even.sort(reverse=True) #you can make the method decide the sorting
# #criteria. list.sort(reverse=True/False)- r=T will sort the list descending.
# #r=F is default.
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even,odd]
print(numbers)

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)
        