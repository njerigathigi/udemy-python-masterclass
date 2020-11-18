#Tuples are similar to lists.The only diff is tuples are immutable(ie cannot be changed)
#items in a tuple are separated by a comma.Parentheses are
#only required to remove syntactic ambiguity.

t = 'a', 'b', 'c' #tuple
print(t)

print('a', 'b', 'c')
print(('a', 'b', 'c')) #tuple

welcome = 'welcome to my nightmare' ,'alice cooper' ,1975
bad = 'bad company' 'bad company' , 1974
budgie = 'nightflight', 'Budgie', 1981
imelda = 'More mayhem', 'Emilda May', 2011
metallica = 'Ride the lightening' , 'Metallica', 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# metallica[0] = 'Master of puppets' #error
imelda_two = imelda[0], 'Imelda May' , imelda[2] #assign a new object to your variable.
print(imelda_two)
print(imelda)

metallica2 = ['Ride the lightening', 'Metallica', 1984]
print(metallica2)
# # metallica[0] = 'Master of puppets'
# metallica2[0] = 'Master of puppets'
# print(metallica2)
#tuples are supposed to hold heterogenous data. lists homogenous(data of the same type)
#to hold immutable data.

title , artist, year = imelda #unpacking the tuple
print(title)
print(artist)
print(year)

# metallica2.append('Rock')
title, artist, year = metallica2 #value error(too many values to unpack-expected 3)

# imelda.append('jazz') #attribute error: 'tuple' object has no attribute 'append'

# imelda = 'More Mayhem', 'Imilda May', 2011 ,(
#     (1, 'Pulling the rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')

# )

# imelda = 'More Mayhem', 'Imilda May', 2011 ,(1, 'Pulling the rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
print(imelda)


imelda = 'More Mayhem', 'Imilda May', 2011 ,1, 'Pulling the rug', 2, 'Psycho', 3, 'Mayhem', 4, 'Kentish Town Waltz'
title , artist , year, track1 , track2, track3, track4 = imelda


print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)
