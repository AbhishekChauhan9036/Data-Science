# String Handling in Python
text = "Hello, World!"
print(text[0])         # Output: H
print(text.lower())    # Output: hello, world!
print(text.upper())    # Output: HELLO, WORLD!


"""
| Method          | Description                         |
| --------------- | ----------------------------------- |
| `lower()`       | Converts to lowercase               |
| `upper()`       | Converts to uppercase               |
| `strip()`       | Removes leading/trailing whitespace |
| `replace(a, b)` | Replaces all `a` with `b`           |
| `split()`       | Splits string into list             |
| `join()`        | Joins list into string              |
| `find()`        | Finds first index of substring      |
"""

# List Comprehensions
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]

numbers = [10, 55, 78, 34]
filtered = [n for n in numbers if n > 50]

evens = [x for x in range(1, 11) if x % 2 == 0]
