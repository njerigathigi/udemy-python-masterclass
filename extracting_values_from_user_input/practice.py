numbers = input("Please enter a series of numbers, using any separators you like: ")
separators = ""
for char in numbers:
    if not char.isnumeric():
        separators = separators + char
print(separators)
