# while True:
#     choice = input("""please choose your option from the list below:
#                 1.Learn Python
#                 2.Learn Java
#                 3.Go swimming
#                 4.Have Dinner
#                 5.Go to bed
#                 0.Quit\n""")
                
#     if choice == "1":
#         print("{} is a Great choice.".format(choice))
#     elif choice == "2":
#         print("{} is a Great choice.".format(choice))
#     elif choice == "3":
#         print("{} is a Great choice.".format(choice))
#     elif choice == "4":
#         print("{} is a Great choice.".format(choice))
#     elif choice == "5":
#         print("{} is a Great choice.".format(choice))
#     elif choice == "0":
#         print("Goodbye!")
#         break
#     else:
#         print("Error: Your choice is out of range!")


# choice = input("please choose your option from the list below:")
# print("1.\tlearn python")
# print("2.\tLearn Java")
# print("3.\tGo swimming")
# print("4.\tHave dinner")
# print("5.\tGo to bed")
# print("0.'\tQuit")

# while True:
#     choice = input()
    
#     if choice == "0":
#         print("Goodbye!")
#         break
#     elif choice in "12345":
#         print("{} is a great choice".format(choice))
#     else:
#         choice = input("please choose your option from the list below:")
#         print("1.\tlearn python")
#         print("2.\tLearn Java")
#         print("3.\tGo swimming")
#         print("4.\tHave dinner")
#         print("5.\tGo to bed")
#         print("0.'\tQuit")

#         choice = input()

choice = input("please choose your option from the list below:")
print("1.\tlearn python")
print("2.\tLearn Java")
print("3.\tGo swimming")
print("4.\tHave dinner")
print("5.\tGo to bed")
print("0.'\tQuit\n")



while choice != "0":
    if choice in "12345":
        print("{} is a great choice.".format(choice))
    else:
        choice = input("please choose your option from the list below:")
        print("1.\tlearn python")
        print("2.\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to bed")
        print("0.'\tQuit")
        
        choice = input()
