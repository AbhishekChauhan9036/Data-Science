print("Hello World!")

#Remove new Line
print("Hello", "World", sep="-", end="!!!\n") 

num = 10
print(num)

pie = 3.1416
print(pie)

# user input
fname = input()
lname = input()
print(fname,lname)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name,age)

# how to check data types
print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>

# type conversion
a = 5
b = float(a)  # Explicit
c = 3.0 + a   # Implicit
