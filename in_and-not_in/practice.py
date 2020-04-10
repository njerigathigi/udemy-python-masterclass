parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot: #if the condition evaluates to true the code executes
    print("{} is in {}.".format(letter, parrot))
else:
    print("i don't need that letter.")
#you can check for longer sequences ie blue etc 
#program is case sensitive
