name = input("Enter your name : ")
age = int(input("How old are you {}? ".format(name)))

if age < 18:
    print("Please come back in {} year(s)".format(18 - age))
    
elif age == 900 :
    print("Sorry, Yoda, you die in return of the Jedi.")
else:
    print("You are old enough to vote.")
    print("Please put an x in the box")
    


