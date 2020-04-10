age = 24
print( "my age is " + str(age) + " years")
print("my age is {0} years".format(age))
print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}."
      .format(31 ,"Jan" ,"March" , "May" , "July" ,"August","October","Dec"))
print("Jan:{1} ,Feb:{0} ,March:{1} ,Apr:{2} ,May:{1} ,June:{2}.".format(28,31,30))
#its the field index , the number inside the curly braces , that determines
#which value to be used.
print("""
Jan:{1} 
Feb:{0} 
Mar:{1} 
Apr:{2} 
May:{1} 
Jun:{2} 
Jul:{1} 
Aug:{1} 
Sep:{2} 
Oct:{1} 
Nov:{2} 
Dec:{1}""".format(28,31,30))
#To create strings that span multiple lines,
# triple single quotes ''' or triple double quotes
# """ are used to enclose the string. 
#''' This string is on multiple lines within three
# single quotes on either side. ''' """ 
#This string is on multiple lines within three double quotes on either side.
