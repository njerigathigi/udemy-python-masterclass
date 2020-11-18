panagram = '''The quick brown 
fox jumps\tover 
the lazy dog'''

words = panagram.split()
print(words)
#split returns a list
#if no argument is provided,it defaults to using whitespaces.
#The split() method splits a string into a list.
#You can specify the separator, default separator is any whitespace.
#whitespaces includes tabs, newlines as well as space.
#it discards any empty strings from the result.

numbers = '9,223,372,036,854,775,807'
print(numbers.split(','))

# values = ''.join(char if char not in separators else '' for char in numbers).split()

generated_list = [
    '9', ' ', '2', '2',
    '3', ' ', '3', '7',
    '2', ' ','0', '3',
    '6', ' ', '8', '5',
    '4', '7', '7'
]

values = ''.join(generated_list)
print(values)

values_list = values.split()
print(values_list)



#  use a for loop to produce a list of ints, rather than strings
#you can either modify the contents of the 'values_list' list in place,
#or create a new list of ints.

#create a new list
new_list = []
for value in values_list:
    new_list.append(int(value))

print(new_list)

#replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)
