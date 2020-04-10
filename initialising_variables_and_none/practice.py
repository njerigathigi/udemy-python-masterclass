shopping_list = ["milk" ,"Pasta" ,"Eggs" ,"Spam" ,"Bread" ,"Rice"]
item_to_find = "milk"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# if found_at is not None:

#     print("Item found at position {}".format(found_at))
# #none is a constant that represents nothing.
# else:
#     print("{} not found.".format(item_to_find))


if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
    

if found_at is not None:
    print("Item found at position {}.".format(found_at))

else:
    print("{} not found".format(item_to_find))

#he index() method searches an element in the list
# and returns its index. In simple terms, the index()
# method finds the given element in a list and returns 
# its position. If the same element is present more than
# once, the method returns the index of the first 
# occurrence of the element.
