answer = 5

print("please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("please guess higher")
    guess = int(input()) # = is an assignment operator
    
    if guess == answer:  # == is a comparison operator.
        print("well done,you guessed it.")
    else:
        print("sorry, you guessed incorrectly.")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    
    if guess == answer:
        print("well done,you guessed it.")
    else:
        print("You guessed incorrectly.")
else:
    print("You got it first time.")

#if blocks can be more complex including if and else blocks
#(and much more) contained within it.
#An if statement can include many elifs but there can only be one else.
#elif is short for else if.
#the else,if there is one,must always come after all the elif blocks.
#Duplicating code is always a bad idea-theres almost always a better way.
