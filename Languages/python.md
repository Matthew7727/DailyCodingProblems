# Python Cheatsheet

## 1. Numbers
### Integers
Whole numbers, e.g., `5`, `-3`

### Floats
Decimal numbers, e.g., `3.14`, `-0.001`

### Common Methods/Operations
```python
# Arithmetic
a + b      # Addition
a - b      # Subtraction
a * b      # Multiplication
a / b      # Division
a // b     # Floor Division
a % b      # Modulus
a ** b     # Exponentiation

# Built-in Functions
abs(x)       # Absolute value
round(x, n)  # Round to n decimal places
pow(a, b)    # a raised to the power of b
divmod(a, b) # Returns (a // b, a % b)

# String Creation
s = "Hello, World!"

# Accessing Characters
s[0]        # 'H'
s[-1]       # '!'
s[0:5]      # 'Hello'

# Common Methods
s.lower()          # 'hello, world!'
s.upper()          # 'HELLO, WORLD!'
s.capitalize()     # 'Hello, world!'
s.title()          # 'Hello, World!'
s.strip()          # Remove surrounding whitespace
s.replace("Hello", "Hi")  # 'Hi, World!'
s.split(", ")      # ['Hello', 'World!']
",".join(['a', 'b', 'c']) # 'a,b,c'

# Checking Content
s.startswith("He") # True
s.endswith("!")    # True
s.isalpha()        # False (includes non-alphabetic characters)
s.isdigit()        # False (not only digits)
s.isalnum()        # False (not alphanumeric)

# List Creation
lst = [1, 2, 3, 4]

# Accessing Elements
lst[0]         # 1
lst[-1]        # 4
lst[1:3]       # [2, 3]

# Common Methods
lst.append(5)       # [1, 2, 3, 4, 5]
lst.extend([6, 7])  # [1, 2, 3, 4, 5, 6, 7]
lst.insert(2, 2.5)  # [1, 2, 2.5, 3, 4, 5, 6, 7]
lst.remove(2.5)     # [1, 2, 3, 4, 5, 6, 7]
lst.pop()           # Removes and returns the last item, [1, 2, 3, 4, 5, 6]
lst.sort()          # Sorts the list in place
lst.reverse()       # Reverses the list in place
lst.index(3)        # 2 (index of the first occurrence of 3)
lst.count(3)        # 1 (count of occurrences of 3)

# List Comprehensions
squared = [x**2 for x in lst]  # [1, 4, 9, 16, 25, 36]

# Tuple Creation
tup = (1, 2, 3, 4)

# Accessing Elements
tup[0]         # 1
tup[-1]        # 4
tup[1:3]       # (2, 3)

# Common Methods (Tuples are immutable, so methods are limited)
tup.count(3)   # 1 (count of occurrences of 3)
tup.index(3)   # 2 (index of the first occurrence of 3)

# Dictionary Creation
d = {"name": "Alice", "age": 25}

# Accessing Elements
d["name"]           # 'Alice'
d.get("name")       # 'Alice'
d.get("address", "Unknown")  # 'Unknown'

# Common Methods
d.keys()            # dict_keys(['name', 'age'])
d.values()          # dict_values(['Alice', 25])
d.items()           # dict_items([('name', 'Alice'), ('age', 25)])
d.update({"age": 26})  # Updates the dictionary, {'name': 'Alice', 'age': 26}
d.pop("age")        # Removes and returns value of 'age', {'name': 'Alice'}
d.clear()           # Clears the dictionary, {}

# Dictionary Comprehensions
squared = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set Creation
s = {1, 2, 3, 4}

# Common Methods
s.add(5)            # {1, 2, 3, 4, 5}
s.update([6, 7])    # {1, 2, 3, 4, 5, 6, 7}
s.remove(3)         # {1, 2, 4, 5, 6, 7}
s.discard(10)       # Removes 10 if it exists, does nothing if not
s.pop()             # Removes and returns an arbitrary element
s.clear()           # Clears the set

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

a | b               # Union: {1, 2, 3, 4, 5}
a & b               # Intersection: {3}
a - b               # Difference: {1, 2}
a ^ b               # Symmetric Difference: {1, 2, 4, 5}

if condition:
    # code
elif another_condition:
    # code
else:
    # code

    # For Loop
for i in range(5):
    print(i)

# While Loop
i = 0
while i < 5:
    print(i)
    i += 1

# Loop Control
for i in range(5):
    if i == 3:
        break       # Exit loop
    if i == 2:
        continue    # Skip to next iteration

    squares = [x**2 for x in range(10) if x % 2 == 0] #[0, 4, 16, 36, 64]

# Single Numbers
max(1, 5, 3)  # 5
min(1, 5, 3)  # 1

# Lists of Numbers
numbers = [4, 1, 7, 3]
max(numbers)  # 7
min(numbers)  # 1

# Single Strings (lexicographical order)
max("apple", "banana", "cherry")  # 'cherry'
min("apple", "banana", "cherry")  # 'apple'

# Lists of Strings
words = ["apple", "banana", "cherry"]
max(words)  # 'cherry'
min(words)  # 'apple'

# Nested Lists
lists = [[3, 4], [1, 2], [5, 6]]
max(lists)  # [5, 6]
min(lists)  # [1, 2]

# Dictionary Keys
d = {"a": 1, "b": 2, "c": 3}
max(d)  # 'c' (lexicographical order)
min(d)  # 'a'

# Dictionary Values
max(d.values())  # 3
min(d.values())  # 1

# Dictionary Items (Tuples)
max(d.items())  # ('c', 3)
min(d.items())  # ('a', 1)

# Sets of Numbers
s = {3, 1, 4, 2}
max(s)  # 4
min(s)  # 1

# Tuples of Numbers
t = (3, 1, 4, 2)
max(t)  # 4
min(t)  # 1

# Example with Key Function
words = ["apple", "banana", "cherry"]

# Find the word with the maximum length
max(words, key=len)  # 'banana'

# Find the word with the minimum length
min(words, key=len)  # 'apple'