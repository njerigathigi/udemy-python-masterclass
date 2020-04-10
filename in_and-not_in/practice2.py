activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But i wanna go to the cinema.")
#The casefold() method is an aggressive lower() method 
#which convert strings to casefolded strings for caseless matching.
#The casefold() method is removes all case distinctions 
#present in a string. It is used for caseless matching, 
#i.e. ignores cases when comparing.
