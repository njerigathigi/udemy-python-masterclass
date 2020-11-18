#when an object is described as immutable , that means it can't be changed.
#built in immutable types in python include-int,float,bool(True/False-a subclass 
# of int, str, tuple, frozenset, bytes)


# result = True
# another_result = result
# print(id(result)) #returns the identity of an object.
# print(id(another_result))

# result = False
# print(id(result))

result = 'correct'
another_result = result
print(id(result))
print(id(another_result))

result += 'ish'
print(id(result))
print(id(another_result))
