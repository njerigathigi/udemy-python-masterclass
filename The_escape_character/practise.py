splitstring = 'this string has been\nsplit over\nseveral\nlines'
print(splitstring)
# \n starts a new line
tabbedstring = '1\t2\t3\t4\t5'
print(tabbedstring)
# \t used for TAB character.it makes a horizontal tab space between two strings or characters
print('The pet shop owner said,"no,no, \'e\'s resting".')
print("The pet shop owner said,\"no,no, 'e's resting\".")
print('''The pet shop owner said,\"no,no, 'e's resting".''')
# with triple quotation marks,you can use both single and double quotes
# backlash can also be used to split a lengthy string.
# the output will still be a single string
anotherstring = print('''This string has been/
split/
over/
several/
lines.''' 
)
# print("c:\users\timbuchalka\notes.txt")
# interprets t as a tab character, n as a line feed character and 
# u is used to include things like accented characters into your strings
print("c:\\users\\timbuchalka\\notes.txt")
# you escape the backlash by putting another backlash before
print(r"c:\users\timbuchalka\notes.txt")
# we use a raw string by prefixing the string with the letter r for raw
