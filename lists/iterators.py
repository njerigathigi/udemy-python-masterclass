#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you
# can traverse through all the values.
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:
#The next() function returns the next item from the iterator.
string = "1234567890"

for character in string:
    print(character)
for character in iter(string):
    print(character)

# my_iterator = iter(string)
# # print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
