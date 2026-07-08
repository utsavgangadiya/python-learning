a=int(input("Enter 1 number :"))
b=int(input("Enter 2 number :"))
c=int(input("Enter 3 number :"))
d=int(input("Enter 4 number :"))


if (a>=b and a>=c and a>=d):
    print(a,"is greatest no")
elif(b>=c and b>=d):
    print(b,"is greatest no")
elif(c>=d):
    print(c,"is gretest no")
else:
    print(d,"is greatest no")