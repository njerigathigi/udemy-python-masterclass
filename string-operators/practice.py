#python has 5 sequence types built in:string,tuple,list,range,
#byte and byte array.
#a sequence is an ordered set of items.
#indexing is very important while dealing with sequences
#because a sequence is ordered ,indices can be used to
#access individual items in a sequence.
computer_parts = ["computer" , "monitor", "keyboard" ,"mouse", "mouse mat"]
print(computer_parts[1])
print(computer_parts[1][0])
#everything you can do with the str datatype can be done with other 
#sequence data types except range.range cannot be concatenated.
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords" )
print("hello " * 5)
# print( "hello " * 5 + 4) #type error
print("hello " * (5 + 4))
print("hello " * 5 + "4")
print()
today = "Friday"
print("day" in today) #True
print("Fri" in today) #True
print("Thur" in today) #False
print("Parrot" in "fjords") #False
print("fjor" in "fjords") #True
