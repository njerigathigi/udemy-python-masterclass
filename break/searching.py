shopping_list = ["Milk" ,"Pasta" ,"Eggs" ,"Spam" ,"Bread" ,"Rice"]
# print(len(shopping_list))

item_to_find = "Spam"
found_at = None
# for index in range(6): 
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Item found at position {}.".format(found_at))



#len() is a built-in function in Python 3. This method returns the 
#length (the number of items) of an object.
