# same value i time 
count = 1
while count<=5:
    print("hello")
    count += 1
print("----------------------------------------------------------------------------")



# reverse even number
i = 10
while i>=1:
    print(i)
    i -= 2
print("----------------------------------------------------------------------------")



# 1 to 100 number print 
i = 1
while i<=100:
    print(i)
    i += 1
print("----------------------------------------------------------------------------")


# multiplication of n number 

# num = int(input("Enter number for multiplication :"))
num = 4
i=1
while (i<=10):
    print(f"{num} * {i} = { i*num}")
    i += 1
print("----------------------------------------------------------------------------")


# print the list num
number=[1,4,8,16,25,36,69,81,99]
idx = 0
while (idx < len(number)) :
    print(number[idx])
    idx += 1

print("----------------------------------------------------------------------------")

# search num in tuple 
 
tuple1 = (1,10,11,20,21,30,31,40)

x = 40

i = 0 
while i < len(tuple1):
    if (tuple1[i]== x):
        print("found at inx ",i)
    i += 1

print("----------------------------------------------------------------------------")


# break

i = 10 
while i >= 1:
    print(i)
    if (i == 7):
        break
    i -= 1

print("loop break")

print("----------------------------------------------------------------------------")


print("continue ex ")

i = 1 
while i <= 10:
    if (i == 5):
        i += 1
        continue
    print(i)
    i += 1


print("loop break")