import random #This module implements pseudo-random 
# number generators for various distributions. 
# For integers, there is uniform selection from a range.
answer = random.randint(1 , 10)
# print(answer)
#random.randint(a, b)¶: Return a random integer N 
#such that a <= N <= b.randint is a function.Must be preceded
#by random. to let python know that its from the random module.
# We separate the module name from the function name by
# using a dot notation.

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
