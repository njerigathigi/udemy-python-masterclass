empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)



# numbers = even + odd
# print(numbers)





# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)

# digits = sorted('432985617') #Sorted() sorts any sequence (list, tuple)
#                              #and always returns a list with the elements 
#                              #in sorted manner, without modifying the original sequence.
# print(digits)

# digits = list('432985617')
# print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
# more_numbers = numbers.copy()
#The copy() method returns a shallow copy of the list. 
# The problem with copying lists in this way is that if you modify
#  new_list , old_list is also modified. 
# print(more_numbers)

# print(id(numbers))
# print(id(more_numbers))
# print(numbers is more_numbers) #not the same list
# print(numbers == more_numbers) #are equal.



# even.extend(odd)
# print(even)
# another_even = even
# print(another_even) 

# even.sort(reverse = True)
# print(even)
# print(another_even)

# print(min(even))
# print(max(even))/ //.
# print(min(odd))
# print(max(odd))


# print()
# print(len(even))
# print(len(odd))


# print()
# print('mississippi'.count('iss')) #A method is bound to an object. we need an object
#                                   #to call a method.
#                                   #we tell it what object it should be using when it
#                                   #performs its function.
