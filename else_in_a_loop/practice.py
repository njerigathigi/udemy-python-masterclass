numbers = [1 ,45 ,15 ,32 ,60]

for number in numbers:
    if number % 8 == 0:
        #reject list
        print("These numbers are unacceptable.")
        break
else:
    print("These numbers are okay.")
