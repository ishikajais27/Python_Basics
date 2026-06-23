# Python Basics - My Learning Documentation

---

## 1. Taking Input

`input()` **always returns a string.** This is the most important thing to remember.

```python
n = int(input())           # single integer
input().split(",")         # comma-separated → list of strings
map(int, input().split(","))  # comma-separated → integers directly
```

For multi-line input until user stops:

```python
while True:
    line = input()
    if line == "":
        break
```

---

## 2. Loops and Conditionals

`range(2000, 3201)` - stop value is **excluded**, so write 3201 to include 3200.

`%` is the modulus operator — used for divisibility checks.

- `i % 7 == 0` → divisible by 7
- `i % 2 != 0` → odd number

Combine conditions with `and` / `or`:

```python
if i % 7 == 0 and i % 5 != 0:
```

---

## 3. Functions and Recursion

```python
def fact(n):
    if n == 0 or n == 1:   # base case — must exist or it loops forever
        return 1
    return n * fact(n - 1) # function calls itself
```

Recursion = function calls itself. Always needs a **base case** to stop. Without it → infinite recursion → crash.

---

## 4. Strings

Strings are **immutable** - you can't change characters, only create new strings.

| Method                      | What it does        |
| --------------------------- | ------------------- |
| `.upper()`                  | all caps            |
| `.split(",")`               | splits into list    |
| `",".join(list)`            | list back to string |
| `.isalpha()`                | only letters?       |
| `.isdigit()`                | only digits?        |
| `.isupper()` / `.islower()` | case check          |

**String as sequence** — you can loop over it character by character:

```python
for ch in sentence:
    if ch.isalpha():
        letters += 1
```

**ASCII comparison** — characters compare by their ASCII value directly:

```python
'a' <= ch <= 'z'   # lowercase check without any method
'A' <= ch <= 'Z'   # uppercase check
```

---

## 5. Lists

Ordered, **mutable** sequence.

```python
arr = []
arr.append(value)       # add to end
arr.insert(0, value)    # add at index 0
arr[0:5]                # slice: first 5 elements
arr[5:]                 # everything from index 5
arr[::-1]               # reverse — step of -1
```

**Why use `temp` for 2D arrays?**
Because you need each row to be a separate list. `temp` stores one complete row first, then you append that whole row to the main array.

**Sorting:**

- `.sort()` → sorts in-place, modifies original
- `sorted()` → returns new list, original unchanged

---

## 6. Tuples

Ordered, **immutable** sequence — data that shouldn't change.

```python
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t[0:5]     # first half
t[5:]      # second half
tuple(list) # convert list → tuple
```

**Python compares tuples left to right automatically** — so sorting a list of `(name, age, score)` tuples just works without a custom comparator.

---

## 7. Dictionaries

Key-value pairs. Keys must be unique.

```python
d = {}
d[key] = value        # add/update
d.keys()              # all keys
d.values()            # all values
d.items()             # key-value pairs
key in d              # check existence — O(1)
```

**Frequency counter pattern:**

```python
if word in freq:
    freq[word] += 1
else:
    freq[word] = 1
```

---

## 8. Sets

Unordered, **no duplicates** — duplicates removed automatically.

```python
words = set(words)     # removes all duplicates instantly
sorted(set)            # returns sorted list of unique elements
```

Use when you care about **membership**, not order.

---

## 9. `map()` and `filter()`

Both return **lazy iterators** — they don't compute until you use them. This is why printing them shows `<map object at 0x...>` not actual values. Wrap in `list()` to get real values.

```python
map(function, iterable)    # applies function to every element
filter(function, iterable) # keeps only elements where function returns True
```

**Lambda** = small anonymous function for use right here, right now:

```python
lambda x: x % 2 == 0   # True if even
lambda x: x ** 2        # square
```

**Combining both:**

```python
even = filter(lambda x: x % 2 == 0, num)   # filter first
squares = map(lambda x: x ** 2, even)       # then transform
```

---

## 10. Classes and OOP

```python
class MyClass:
    class_param = "shared"          # belongs to ALL objects

    def __init__(self, value):
        self.instance_param = value  # unique to each object
```

**Class parameter** → shared across all instances.
**Instance parameter** → unique to each object, defined in `__init__` with `self`.

If both exist with the same name, the instance parameter **shadows** the class one for that object.

### Static Method

```python
@staticmethod
def method():
    ...
```

Belongs to the class, not any object. No `self`. Called directly: `ClassName.method()`. Just a utility function living inside a class.

### Generator with `yield`

```python
def generate(self, n):
    for i in range(n + 1):
        if i % 7 == 0:
            yield i   # pauses here, gives value, resumes next call
```

`yield` pauses the function and hands one value to the caller. Resumes from the same spot next time. Memory efficient — produces values one at a time, not all at once.

---

## 11. Binary → Decimal Conversion

**With method:**

```python
int("1010", 2)   # second argument = base
```

**Without method (manual):**

```python
decimal = 0
power = 0
for j in binary_string[::-1]:   # read right to left
    decimal += int(j) * (2 ** power)
    power += 1
```

---

## 12. Distance Formula (Robot Problem)

Two variables track position — `x` for left/right, `y` for up/down.

- UP → `y += step`, DOWN → `y -= step`
- RIGHT → `x += step`, LEFT → `x -= step`

Distance = Pythagorean theorem:

```python
distance = ((x**2) + (y**2)) ** 0.5
print(round(distance))
```

---

## 13. Password Validation Pattern

Boolean flags — one per condition, all start `False`. Loop through each character and flip the right flag. At the end, all must be `True`.

```python
lower = upper = digit = special = False
for ch in password:
    if 'a' <= ch <= 'z': lower = True
    elif 'A' <= ch <= 'Z': upper = True
    elif '0' <= ch <= '9': digit = True
    elif ch in "$#@": special = True

if lower and upper and digit and special:
    # valid
```

---

## 14. `__doc__` — Documentation

Every function can have a docstring as its first line. Access it with `.__doc__`.

```python
def square(n):
    """Returns square of a number"""
    return n ** 2

print(square.__doc__)   # Returns square of a number
print(abs.__doc__)      # Python's own built-in documentation
```

---

## 15. Core Concepts to Always Remember

| Concept                 | Key Point                                   |
| ----------------------- | ------------------------------------------- |
| `input()`               | Always returns string — always cast         |
| `range(a, b)`           | b is excluded — write b+1 to include b      |
| Recursion               | Must have a base case                       |
| `map()` / `filter()`    | Lazy — wrap in `list()` to see values       |
| List vs Tuple           | List = mutable, Tuple = immutable           |
| `.sort()` vs `sorted()` | In-place vs returns new list                |
| Set                     | Removes duplicates automatically            |
| `self`                  | Refers to the current object inside a class |
| `yield`                 | Pauses function, resumes next call          |

---

## 16. OOP — Inheritance and Subclasses

`class Subclass(ParentClass)` defines a subclass that inherits everything from the parent.

The subclass gets all parent methods for free. It can also add its own new methods.

**Parent class** = original class that contains variables and methods.
**Subclass** = class that inherits everything from the parent class.

---

## 17. Classes — Methods with Parameters

Methods can accept parameters just like regular functions. `self` always comes first.

You pass values when calling: `c.area(r)` or `r.area(length, width)`.

---

## 18. Method Overriding (Polymorphism)

Define a method with the **same name** in the subclass to override the parent's version.

Python always calls the most specific version — the subclass method wins.

To override a method in super class, define a method with the same name in the subclass.

---

## 19. Raising Exceptions with `raise`

`raise` lets you manually trigger an error. Used inside conditions to enforce rules.

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

Types of built-in exceptions: `ValueError`, `TypeError`, `RuntimeError`, `ZeroDivisionError`, etc.

| Concept       | Key Point                                              |
| ------------- | ------------------------------------------------------ |
| Syntax Error  | Caught before running — bad code structure             |
| Runtime Error | Happens during execution after code starts             |
| `raise`       | You create the error yourself — usually inside an `if` |

---

## 20. `try` / `except` — Catching Errors

`try` block: Python attempts to run this.
`except` block: runs only if an error occurs — prevents crash.

```python
try:
    divide()
except ZeroDivisionError:
    print("Cannot divide by zero")
```

`except` catches by error type. Multiple `except` blocks can catch different error types.

---

## 21. Custom Exception Classes

Inherit from `Exception` to make your own error type.

```python
class CustomError(Exception):
    pass
```

With a constructor (to store a message):

```python
class AgeError(Exception):
    def __init__(self, message):
        self.message = message
```

`as e` gives you access to the exception object so you can read its attributes.

Three ways to define custom exceptions:

- **Method 1:** `class MyError(Exception): pass` — simplest
- **Method 2:** Custom Exception with `__init__` constructor to store message
- **Method 3:** Inherit from another built-in exception like `ValueError`

---

## 22. Regex — `re` Module

`re` = Regular Expression. A Python module used for: searching text, finding patterns, matching strings.

| Pattern | Meaning                                  |
| ------- | ---------------------------------------- |
| `\w`    | Any word character (letters, digits, \_) |
| `\d`    | Any digit (0–9)                          |
| `+`     | One or more of the previous              |
| `\.`    | Literal dot (escaped)                    |

```python
re.match(r"(\w+)@\w+\.com", email)  # match from start of string
m.group(1)                           # first captured group — inside first ()
re.findall(r"\d+", text)             # returns list of all matches
```

`group(1)` = first `()` in the pattern. `group(0)` = entire match.

`re.findall()` — finds all matches and returns them as a list.

---

## 23. Unicode Strings

In Python 3, all strings are Unicode by default. `u"..."` prefix is optional but valid.

```python
print(u"hello world")   # works
print(u"नमस्ते")         # non-English characters work too
```

To convert a string to bytes using UTF-8 encoding:

```python
s.encode("utf-8")       # string → bytes
bytes.decode("utf-8")   # bytes → string back
```

`encode()` and `decode()` are inverse operations. `zlib`, file I/O, and network code work with bytes, not strings.

`utf-8` = Unicode Transformation Format - 8 bit. A very popular encoding method.

In Python 3, `unicode()` does not exist — use `encode()` instead.

---

## 24. Math Series — Fractional Sums

Pattern: compute `i/(i+1)` for `i` from 1 to n.

```python
total = 0
for i in range(1, n + 1):
    total += float(i) / (i + 1)
```

`float(i)` forces true division. Use `round(total, 2)` to limit decimal places.

---

## 25. Recursion — Custom Formula

`f(n) = f(n-1) + 100`, `f(0) = 1`

Always define: **base case first**, then recursive case. The base case is what stops the recursion.

---

## 26. Fibonacci Sequence

`f(0) = 0`, `f(1) = 1`, `f(n) = f(n-1) + f(n-2)`

To print as comma-separated sequence using list comprehension + join:

```python
result = [fibonacci(i) for i in range(n + 1)]
print(",".join(map(str, result)))
```

`map(str, result)` converts each number to string so `join()` can work on it.

---

## 27. Generators with `yield`

A generator function uses `yield` instead of `return`. It gives one value at a time and pauses.

| Concept   | Behavior                                         |
| --------- | ------------------------------------------------ |
| `return`  | Gives everything at once and stops               |
| `yield`   | Gives one value, pauses, resumes next call       |
| `list()`  | Computes everything immediately (eager)          |
| generator | Computes one at a time (lazy) — memory efficient |

To print comma-separated output from a generator:

```python
for i in gen(n):
    print(i, end=",")
```

---

## 28. `assert` Statement

`assert` checks that a condition is `True`. If `False`, it raises `AssertionError`.

```python
assert n % 2 == 0    # passes if n is even, raises AssertionError if odd
```

Use inside `try/except` to handle assertion failures gracefully.

---

## 29. `eval()` — Dynamic Expression Evaluation

`eval()` takes a string and runs it as Python code. Returns the result.

```python
result = eval("35+3")   # returns 38
```

Use with caution — only on trusted input. Never use `eval()` on user input in production systems.

---

## 30. Binary Search

Searches a sorted list by repeatedly halving the search space. **O(log n)**.

```python
low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2
    if a[mid] == target:
        return mid
    elif a[mid] > target:
        high = mid - 1    # go left
    else:
        low = mid + 1     # go right

return -1                 # not found
```

Always returns index of found element or `-1` if not found.

---

## 31. Random Numbers — `random` Module

| Method                   | What it does                              |
| ------------------------ | ----------------------------------------- |
| `random.random()`        | Float between 0 and 1                     |
| `random.choice(list)`    | One random element from a list            |
| `random.sample(list, n)` | n unique random elements from a list      |
| `random.randrange(a, b)` | Random integer from a to b-1 (b excluded) |
| `random.shuffle(list)`   | Shuffles list in place, returns `None`    |

Scaling `random.random()` to a range:

```python
random.random() * 90 + 10   # float between 10 and 100
```

Formula: `random.random() * (max - min) + min`

Divisible by both 5 and 7 = divisible by **35** (LCM).

`random.shuffle()` modifies the list in place and returns `None`.

---

## 32. `zlib` — Compression

`zlib` works only with bytes, not strings. Convert first.

```python
compressed = zlib.compress(text.encode())            # str → bytes → compressed
decompressed = zlib.decompress(compressed).decode()  # compressed → bytes → str
```

`encode()` = string to bytes. `decode()` = bytes to string. These are always paired.

---

## 33. `timeit` — Measuring Execution Time

```python
from timeit import timeit
print(timeit("1+1", number=100))
```

Returns a float in seconds. First argument is the code as a string. `number=` is how many times to run it.

`timeit` is a Python module used to measure how long a piece of code takes to execute.

---

## 34. Sentence Generation — Nested Loops

Use nested `for` loops with index access to combine elements from multiple lists.

Total combinations = `len(subjects) × len(verbs) × len(objects)`.

---

## 35. List Comprehension — Filtering

Remove elements that match a condition by keeping only those that don't.

```python
result = [x for x in nums if x % 2 != 0]                              # remove even numbers
result = [x for x in nums if not (x % 5 == 0 and x % 7 == 0)]        # remove divisible by 5 and 7
```

`not (...)` inverts the filter — keep everything that does **NOT** match the removal condition.

---

## 36. `enumerate()` — Index + Value Together

`enumerate()` is a built-in Python function that adds an index to each element of an iterable.

```python
for i, x in enumerate(nums):
    if i % 2 != 0:
        result.append(x)
```

Returns `(index, value)` pairs. Use when you need to filter or act based on **position**.

---

## 37. List `remove()` Method

`remove(value)` deletes the **first occurrence** of that value from the list.

```python
lst.remove(24)   # removes first 24 found
```

Use list comprehension to remove **all** occurrences:

```python
result = [x for x in lst if x != 24]
```

---

## 38. Set Operations — Intersection

`set()` converts a list into a set (removes duplicates, unordered).
`&=` keeps only elements common to both sets.

```python
s1 = set(list1)
s1 &= set(list2)   # s1 now contains only shared elements
```

Other set operators: `|` for union, `-` for difference, `^` for symmetric difference.

---

## 39. Remove Duplicates — Preserve Order

Using `set()` alone doesn't preserve order. Use `seen` set + `result` list:

```python
seen = set()
result = []

for x in lst:
    if x not in seen:
        seen.add(x)
        result.append(x)
```

Quick version (order **not** guaranteed):

```python
print(list(set(lst)))
```

---

## 40. Counting Characters with Dictionary

Use a `dict` as a frequency counter.

```python
d[ch] = d.get(ch, 0) + 1
```

`d.get(key, 0)` returns `0` if key doesn't exist yet — avoids KeyError.

`sep=""` in `print()` removes the default space between arguments.

---

## 41. String — Reverse Words

Split string into words → reverse list → join back.

```python
words = s.split()         # "rise to vote sir" → ['rise', 'to', 'vote', 'sir']
" ".join(words[::-1])     # "sir vote to rise"
```

`s.split()` without arguments splits on any whitespace and removes empty strings.

---

## 42. String — Even Index Characters

`s[::2]` — start from 0, take every 2nd character (step=2).
