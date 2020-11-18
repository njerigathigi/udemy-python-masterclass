# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150, 160,
        # 170, 183, 185, 187, 188, 191]

# data = [1041, 1051, 1101, 1201, 1301, 1501, 1601,
#         1701, 1831, 1851, 1871, 1881, 1911]

data = []

     





min_valid = 100
max_valid = 200
stop = 0

#process low values in the list.works for sorted data
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
#don't change data inside the loop. Change data only after the loop terminates
print(stop)
del data[:stop]
print(data)

# process the high values in a list

start = 0
for index in range(len(data) -1 , -1 , -1): #use -1 instead of 0. -1 tells python to move 1 step backwards
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)







# del data[0:2]
# print(data)
# # del data[-2:]
# del data[14:]
# print(data)

# min_valid = 100
# max_valid = 200

# for index , value in enumerate(data):
#     if value < 100 or value > 200:    #won't work.Be careful with changing the size 
#                                       #of an object that you're iterating over.
                                     
#         del data[index]

# print(data)
