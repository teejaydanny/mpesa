my_tuple = (154, 514, 8714, 546844, 5684894)
print(my_tuple)
print(my_tuple[2])
print(my_tuple[1:4])
print(len(my_tuple))
del my_tuple
# print(my_tuple)
my_tuple2 = (154, 514, 8714, 'cooking', 'fishing', 514564, 156+456 )
if 'cooking' in my_tuple2:
    print('yes', 'cooking is present')
else:
    print('no', 'cooking is absent')

print(max(my_tuple2))
print(min(my_tuple2))
print(sum(my_tuple2))
print(sum(my_tuple2)/len(my_tuple2))
print(my_tuple2)
print(my_tuple2.index(445))
if 445 in my_tuple2:
    print('445 is present in my_tuple2')
else:
    print('445 is not present in my_tuple2')


