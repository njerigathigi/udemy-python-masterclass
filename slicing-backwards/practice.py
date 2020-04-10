letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)
print()
# backwards = letters[25:-1:-1]#no output
# print(backwards)
# backwards = letters[25::-1]#defaults to the start
# print(backwards)
backwards = letters[::-1]#defaults to the start and end
print(backwards)