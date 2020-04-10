answer = 5

print("please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time.")

    #elif must always follow the if block
    #else must always come after the if and elif block
    #as it captures everything else.
    