# Dictionaries in Python
employee = {"id": 101, "name": "John", "department": "HR"}
print(employee["name"])  # Output: John

"""
| Method          | Description                 |
| --------------- | --------------------------- |
| `dict.keys()`   | Returns all keys            |
| `dict.values()` | Returns all values          |
| `dict.items()`  | Returns all key-value pairs |
| `dict.get(key)` | Returns value or None       |
| `dict.update()` | Updates dictionary          |
| `del dict[key]` | Deletes a key-value pair    |
"""



# Sets in Python
even_numbers = {2, 4, 6, 8}
even_numbers.add(10)
print(even_numbers)  # Output: {2, 4, 6, 8, 10}

"""
| Operation                | Description                           |
| ------------------------ | ------------------------------------- |
| `add()`                  | Adds an element                       |
| `remove()` / `discard()` | Removes an element                    |
| `union()`                | Combines two sets                     |
| `intersection()`         | Elements common to both sets          |
| `difference()`           | Elements in one set but not the other |
"""


"""
| Feature    | Dictionary          | Set                   |
| ---------- | ------------------- | --------------------- |
| Structure  | Key-Value pairs     | Unique values only    |
| Indexing   | Keys                | Not supported         |
| Duplicates | Keys must be unique | No duplicates allowed |
| Mutable    | Yes                 | Yes                   |
"""