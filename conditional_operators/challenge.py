answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time.")
else:
    if guess < answer:
        print("Please guess higher")
    else:  #guess must be higher
        print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done,you got it right.")
    else:
        print("Sorry,you guessed incorrectly.")
 