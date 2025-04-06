#common


a = [1,2,3,4,5,6]
b = [2,3,7,8,9]

#unique  in a
lst1 = [x for x in a if x not in b]
print(lst1)

# common in both

lst2 = [y for y in a if y in b]
print(lst2)

# unique in b

lst3 = [z for z in b if z not in a ]
print(lst3)

# unique in both 

lst4 = lst1+lst3
print(lst4)