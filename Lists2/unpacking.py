a = b = c = d = e = f = 42 #useful shortcut
                           #easier to make changes
                           #reduces the amount of code.
print(c)

x , y, z = 1 , 2, 76  #multiple assignment.
print(x , y, z)

data = 1, 2, 76 #unpacking a tuple
x, y, z = data
print(x)
print(y)
print(z)

#you can unpack any sequence type
print('unpacking a list')
data_list = [12, 13, 14]
data_list.append(15)
p, q, r = data_list #give the error(too many values to unpack).
                    #unpacking a tuple is safer because you always 
                    #know how many items you're unpacking.(always successful)
print(p)
print(q)
print(r)
