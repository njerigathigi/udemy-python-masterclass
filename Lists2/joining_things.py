flowers = [
    'Daffodil',
    'Evening Primrose',
    'Hydrangea',
    'Iris',
    'Lavender',
    'Sunflower',
    'Tiger Lily',
    # 42,            #will fail because lists are typically used to store
                     #homogenous items.
]

# for flower in flowers:
#     print(flower)
    
# print(',\n'.join(flowers))

separator = ','
output = separator.join(flowers)
print(output)
#join iterates over a sequence and joins its contents into a string by using a separator.
#it can only join items of one type/kind.

#The join() method returns a string in which the string elements of 
# sequence have been joined by str separator.
