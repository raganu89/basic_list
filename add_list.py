a = [1,2,3,4]
b = [2,3,4,5]
c= []

length = 0
for _ in a:
    length+=1

print(length)

i =0
while i<length:
    sum = a[i]+b[i]
    c.append(sum)
    i +=1

print(c)




