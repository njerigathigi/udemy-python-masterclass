for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}."
           .format(i ,i **2 ,i**3))
           #specify field width by using a colon followed by the field number.
print()

for i in range(1,13):
    print("No. {0:<2} squared is {1:^3} and cubed is {2:>4}."
           .format(i ,i **2 ,i**3))
#< alighs to the left ^aligns at the center > aligns to the right
print()
print("pi is approximately {0:12}".format(22/7))
print("pi is approximately {0:12f}".format(22/7)) # defaults to 6 decimal points 
print("pi is approximately {0:12.50f}".format(22/7)) #not possible to print a 5o digit figure in a field width of 12.python chooses precision and ignores the field width.
print("pi is approximately {0:52.50f}".format(22/7)) #maximum precision number of python floating point numbers is between 51 and 53. 
print("pi is approximately {0:62.50f}".format(22/7))
print("pi is approximately {0:72.50f}".format(22/7))