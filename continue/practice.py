#A list is an ordered set of values enclosed in square brackets
shopping_list = ["Milk" , "Pasta" , "Eggs" , "Spam" , "Bread" , "Rice"]

for item in shopping_list:
    if item != "Spam":
         print("Buy " + item)
print()

for item in shopping_list:
    if item == "Spam":
        continue
    print("Buy " + item) #not in if statement because 
    #its not controlled by it.

#continue statement. The continue statement in Python
# returns the control to the beginning of the current loop.
# When encountered, the loop starts next iteration without 
# executing the remaining statements in the current 
# iteration. The continue statement can be used in both 
#while and for loops.
print()

for letter in "Django":
    if letter == "D":
        continue
    print( f"current letter:{letter}")

