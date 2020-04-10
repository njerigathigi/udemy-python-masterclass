# while True:
#     import random
#     answer = random.randint(1, 10)
#     # print(answer)
#     guess = int(input("Guess a number between 1 and 10 (Quit by entering 0): "))
    
#     if guess== answer:
#         print("You got it first time.")
#         break
#     elif guess < answer and guess != 0:
#         print("Please guess higher.")
#     elif guess > answer:
#         print("Please guess lower.")
#     elif guess == 0:
#         break

import random
answer = random.randint(1 , 10) 
print(answer)
guess = int(input("Guess a number between 1 and 10(Enter 0 to quit): ")) 

    
while guess != answer:
    

    # if guess == answer:
    #     break
    if guess < answer and guess != 0:
        print("Please guess higher.")
        guess = int(input())
        
    elif guess > answer:
        print("Please guess lower.")
        guess = int(input())
        
    elif guess == 0:
        break
