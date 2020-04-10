name = input("Enter your name: ")
age = int(input("How old are you? "))

if age >= 18 and age < 31: #also 18 >= age < 31: 
    print("Welcome for the holiday {0}!".format(name))
else:
    print("Sorry {0}, Maybe next time.".format(name))
