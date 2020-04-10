low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low,high))
input("Press ENTER to start")

guesses = 1

while True:
    guess = low + (high - low) // 2 # // is floored division.
    #truncates answer to an integer
    high_low = input("My guess is {}. Should i guess higher or lower?"
                     "Enter h or l, or c if my guess was correct: "
                     .format(guess)).casefold()
    
    if high_low == "h":
        #guess lower
        low = guess + 1
    elif high_low == "l":
        #guess higher
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))  
        break  
    else:
        print("Please enter h,l or c")
    
    guesses += 1
    