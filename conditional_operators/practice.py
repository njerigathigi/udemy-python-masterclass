#(value comparison operators)
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# == equal to
# != not equal to

answer = 5

print("please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer :
    if guess < answer :
        print("Please guess higher")
    else: # guess must be higher
        print("please guess lower")
    guess = int(input()) # not dependent on the previous conditions
    if guess == answer:
        print("Well done, You guessed it.")
    else:
         print("sorry, You guessed incorrently.")
else:
    print("You got it first time.")

         


#comments are ignored by the python interpreter
# they are there to document your code
#prevent code from being executed
#use them to explain why you've done something in a certain way
#or as a reminder of certain conditions and variable states
#that may not be so obvious.
#they can appear on their own line or at the end of code.