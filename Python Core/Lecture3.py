# Functions
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))  # Output: 120


# Lambda Functions
square = lambda x: x * x
print(square(6))  # Output: 36


# map()
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8]


# filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


# reduce()
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 10


# *args (Non-keyword Arbitrary Arguments)
def total_sum(*args):
    result = 0
    for num in args:
        result += num
    return result

print(total_sum(10, 20, 30))  # Output: 60



# **kwargs (Keyword Arbitrary Arguments)
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Alice", age=20, course="Python")
# Output:
# name: Alice
# age: 20
# course: Python
