# Take input from the user and print length 

str=input("Enter your name :")

print(len(str))

# find occurrence of @ in a string 

string = "$ Hello my name$ is utsav"
print(string.count("$"))

# Reverse Words in a Given String in Python

s = "Python is fun"
res = (s.split()[::-1])
print(type(res))
res = ' '.join(s.split()[::-1])
print(res)

# Swap commas and dots in a String

t = str.maketrans(',.', '.,')
str = "89, 6392, 673.280"


res = str.translate(t)
print(res)

