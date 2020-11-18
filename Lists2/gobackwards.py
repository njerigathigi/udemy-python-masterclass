#iterating backwards is a valuable technique that aloows the size of
#your sequence to be changed without causing a problem.


data = [104, 101, 4, 105, 308, 103, 5, 
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index , data)
#         del data[index] 


top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
        print(top_index- index, value)
        del data[top_index - index]
#more efficient with large data because of enumerate
#easier to understand



 

# for number in data:
#         print(number)
    
# print(data)

#shorter code reduces the chance of having bugs in the program


# data = [1, 2, 3, 4]

# min_valid = 2
# max_valid = 3

# for index in range(len(data)-1, -1, -1):
#         if data[index] < min_valid or data[index ]> max_valid:
#                 del data[index]

# print(data)