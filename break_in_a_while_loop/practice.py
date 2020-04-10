available_exits = ["North" ,"South" ,"East" ,"West"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over.")
        break

print("Aren't you glad you're out of there")
#The casefold() method is an aggressive lower() method
# which convert strings to casefolded strings for caseless
# matching. The casefold() method is removes all case 
# distinctions present in a string. It is used for 
# caseless matching, i.e. ignores cases when comparing.
