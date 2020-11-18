computer_parts = ["computer", 
                  "monitor", 
                  "keyboard", 
                  "mouse", 
                  "mouse mat"
                  ]

print(computer_parts)

# computer_parts[3] = 'trackball'
print(computer_parts[3:])
computer_parts[3:] = ['trackball'] # replaced by contents of the iterable. compare with = 'trackball'
print(computer_parts)





# for part in computer_parts:
#     print(part)

# print()
# print(computer_parts[2])

# print(computer_parts[0:3]) #slicing a list
# print(computer_parts[-1])
# #diff between lists and strings- strings are immutable. lists are mutable ie contents can be changed