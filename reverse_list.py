#1 approach

a= [1,2,3,4,5,6]
a.reverse()
print("approach1:",a)

# 2 approach

a= [1,2,3,4,5,6]
result = a[::-1]
print("approach2:",result)

# 3 approach

a= [1,2,3,4,5,6]
result = []   # empty list to save reverse list

for i in a:
    result = [i]+ result
print("approach3:",result)
