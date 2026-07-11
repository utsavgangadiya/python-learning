set1={0,1,2,3,4,5,True,False}
print(set1)

emptyset = set()
print(type(emptyset))
print(emptyset)

#we can not pass the list and dictionary only tuple can be add in set 
set1.add("python")

set1.add((11,12,13))

set1.remove(3)

print(len(set1))

print(set1)


