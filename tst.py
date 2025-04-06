#unique
L1 = ["a","b","c","d","e","b","k"]
      
L2 = ["b","d","f","k","d"]


result = [x for x in L1 if x not in L2]
print (result)      