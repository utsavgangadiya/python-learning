list1=[1,2,3,4,5,6]

for element in list1:
    print(element)

print("------------------------------")

str ="utsav gangadiya"

for char in str :
    print(char)

print("------------------------------")

num = (10,20,90,30,40,50,60,70,80,90,100)
x=90

idx = 0
for el in num :
    if (el == x):
        print("targeted number found at idx -", idx )
    idx +=1

print("------------------------------")


for el in range(0,11,2) :
    print(el)

# n = int(input("Enter number:"))
n = 44
for el in range(1,11):
    print(f"{el} * {n} = {n*el}")

print("------------------------------")


for el in range(10):
    pass

print("pass")

print("------------------------------")

n = 10
sum = 0
for i in range (1 , n+1):
    sum += i

print(" sum of number ",sum) 

print("------------------------------")

print("factorial")

num = 10
fac = 1
i=1

while i<= 5:
    fac *= i 
    i += 1




print("factorial of",fac)