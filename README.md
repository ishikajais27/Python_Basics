
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

| Method | What it does |
|---|---|
| `.upper()` | all caps |
| `.split(",")` | splits into list |
| `",".join(list)` | list back to string |
| `.isalpha()` | only letters? |
| `.isdigit()` | only digits? |
| `.isupper()` / `.islower()` | case check |

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

| Concept | Key Point |
|---|---|
| `input()` | Always returns string — always cast |
| `range(a, b)` | b is excluded — write b+1 to include b |
| Recursion | Must have a base case |
| `map()` / `filter()` | Lazy — wrap in `list()` to see values |
| List vs Tuple | List = mutable, Tuple = immutable |
| `.sort()` vs `sorted()` | In-place vs returns new list |
| Set | Removes duplicates automatically |
| `self` | Refers to the current object inside a class |
| `yield` | Pauses function, resumes next call |
