# File Handling in Python

"""
File handling lets you read from and write to files.
Common modes:
"r" = read (default)
"w" = write (overwrite)
"a" = append (add at end)
"r+" = read and write
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


"""
| Method        | Description                 |
| ------------- | --------------------------- |
| `open()`      | Opens a file                |
| `read()`      | Reads entire content        |
| `readline()`  | Reads one line at a time    |
| `readlines()` | Reads all lines into a list |
| `write()`     | Writes to a file            |
| `close()`     | Closes the file             |
"""


# Exception Handling in Python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result is:", result)
finally:
    print("Execution finished.")
