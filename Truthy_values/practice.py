#An object can be tested for truth value for use in
#an if  or while condition.
#booleans defined to be False - None , False,
#0 of any numeric type.- False
#Empty sequences and conditions - False.

if 0:
    print("True")
else:
    print("False")
name = input("PLease enter your name: ")
# if name:
if name != "":
    print("Hello,{}.".format(name))
else:
    print("Are you the man/woman with no name?")
