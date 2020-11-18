shopping_list = ['milk',
                 'pasta',
                 'eggs', 
                 'spam', 
                 'bread',
                 'rice'
                 ]
# print(shopping_list)
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ['cookies']

print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list #chained assignment
print(a)
print('adding cream')

b.append('cream')
print(c)
print(d)

#lists are mutable ie the contents of a list can be changed,without creating new 
#references to the same object.
