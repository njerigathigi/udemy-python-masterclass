menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam' ],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
]

#write code to print out all the meals in the menu, but with spam removed.
#choose which approach to use.ie
#remove spam from each list, then print the list or
#print out the items in each list, as long as its not spam
#produce 8 meals, all without spam.

# for meal in menu:
#     if 'spam' in meal:
#         new_menu = []
#         for item in meal:
#             if item == 'spam':
#                 pass
#             else:
#                 new_menu.append(item)
#         print(new_menu)   
        
#     else:
#         print(meal)

# print()
# print()

# for meal in menu:
#     if 'spam' not in meal:
#         print(meal)
#     else:
#         top_index = len(meal) - 1
#         for index, item in enumerate(reversed(meal)):
#             # print(top_index - index, item)
#             if item == 'spam':
#                 del meal[top_index - index]
#         print(meal)

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == 'spam':
            del meal[index]
    print(meal)

# for meal in menu:
#     for item in meal:
#         if item != 'spam':
#             print(item, end = ', ')
#     print()
