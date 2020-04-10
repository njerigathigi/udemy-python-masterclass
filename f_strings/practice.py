name = "Njeri "
age = 25 
# print(name + "is " + age + "years old.") #type error
print(name + f"is {age} " + "years old.")# use f just like formatting.its much neater
#alternatively
print(name + f"is {age} years old.")
print(f"pi is approximately {22/7:52.50f} ")
pi = 22/7
print(f"pi is approximately {pi:12.50f}")
#f strings use replacement fields
#same operations used in formatting can be used with fstrings
