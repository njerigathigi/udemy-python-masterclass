# t = 'a', 'b', 'c'  #tuple
# t = ('a','b', 'c') #also a tuple
# print(t)

welcome = 'welcome to my nightmare' ,'alice cooper' ,1975
bad = 'bad company' 'bad company' , 1974
budgie = 'nightflight', 'Budgie', 1981
imelda = 'More mayhem', 'Emilda May', 2011
metallica = 'Ride the lightening' , 'Metallica', 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = 'master of puppets' #tuples are immutable
                                   #gives an error

#Because tuples dont have the overhead of the methods
#needed to change them, tuples use less memory than lists.
#can also be used when you need to protect the integrity of
# your data. ie incorrect data can be fatal eg when medicine is involved.
#using tuples can help to prevent bugs i your system.

metallica2 = list(metallica)
print(metallica2)
metallica2[0] = 'master of puppets'
print(metallica2)
