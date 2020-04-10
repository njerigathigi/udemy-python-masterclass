available_exits = ["North" ,"South" ,"East" ,"West"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
print("Aren't you glad you're out of there")

#While loops can be used when you cant determine
#in advance how many times you need to loop.
#A for loop will repeat for each item in a pre-determined
#sequence whereas in a for loop you dont need to know how
#many times the loop will execute.
#ie reading data from a file or an internet stream.
