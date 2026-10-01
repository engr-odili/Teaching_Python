# 001 VARIABLES AND DATA TYPES
---
In the last lesson we met variables briefly. Now we go deep. By the end of this
lesson you will understand what a variable really is, what types Python has, how
to convert between them, ans when to use which type.

Every example will use *type hints*, and i will explain as we go.

##1. What is a variable, realy?
A variable is a *name that points to a value stored in memory*.

Think of it like a labeled box:
```text
name --> "Chinedum"
age --> 10
height --> 1.75
```
You do not need to declare the type in advance. Python figures it out when the
program runs. This is called *dynamic typing*

```python
name: str = "Chinedum"
age: int = 10
```
the `: str` and `: int` are *type hints*. They tell humans and tools what you
intend. Python itseld does not enforce them.

You can reassign a variable to a different value, even a different type:
```python
value: int = 10
value = "ten"   # type hint said int, but Python allows this
```
This runs. But `mypy` would warn you. In professional code, do not do this.

##2. Dynamic typing vs type hints
| Concept | Meaning|
|---------|--------|
| Dynamic typing | Python decides the type at runtime |
| Type hints | You write the intended type for clarity and tools |
| Runtime enforcement | Python does *not* enforce hints |
| Static checkers | Tools like `mypy`, `pyright` check hints |

Why use type hints if Python ignores them?
- Your editor gives better autocomplete.
- Bugs are caught before running.
- Other developers understand your code faster
- it forces you to think about your data.

*Where to use them:* always on function parameters and return values. On
variables, use them when the type is not obvious.
*When not to bother:* inside a tiny script, or when the value is obvious like
count: int = 0. Even then, many teams still use them for consistency.

##3. The core built-in types
Python has many types. These are the ones you must know first.
*`int` - Whole numbers*
```python
age: int = 10
temperature: int = -10
population: int = 8_000_000_000   # underscores for readability
```
- No decimal point.
- Can be positive, negative, or zero.
- Python integers can be arbitrarily large (unlike many languages).

*`foat` - Decimal numbers*
```python
price: float = 19.99
pi: float = 3.14159
scientific: float = 1.5e3   # 1500.0
```
- Has a decimal point ou uses scientific notation
- Used for measurements, money (carefully), science.
- Floating point math is not always exact:
```python
result: float = 0.1 + 0.2
print(result)    # 0.30000000000000004
```
For money, use `decimal.Decimal` later we will cover that in future topic.

*`str` - Text*
```python
name: str = "Chinedum"
message: str = 'Hello'
multiline: str = """This is a multi-line string"""
empty: str = ""
```
- Text inside single, double, or triple quotes.
- Strings are immutable - you cannot change them in place.
```python
greeting: str = "Hello"
# greeting[0] = "J"   # TypeError
new_greeting: str = "J" + greeting[1:]
print(new_greeting)  # Jello
```

Common string operatins:
```python
name: str = "Chinedum"
print(len(name))                # 8
print(name.upper())             # CHINEDUM
print(name.lower())             # chinedum
print(name.replace("C", "Q"))   # Khinedum
print(name + " Odili")          # Chinedum Odili
print(f"Hi {name}")             # Hi Chinedum
```

*`bool` - True or False*
```python
is_student: bool = True
has_paid: bool = False
```
- Only two values: `True` and `False`
- Note the capital letters.
- Used in conditions.
```python
is_raining: bool = True
if is_raining:
    print("Take an umbrella")
```
Boolean behave like integers in math (`True == 1`, `False == 0`), but do not
rely on that in normal code.

*`None` - no value*
```python
middle_name: None = None
```
- `None` means "nothing" or "no value yet".
- Its type is `NoneType`
- Useful when a value is optional or missing.
```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Chinedum"
    return None
```
`str | None` means "a string or None". This is modern way (Python 3.10+). We
will cover it more later.

##4. Checking and converting types
*Checking type*
```python
age: int = 10
print(type(age))                  # <class 'int'>
print(isinstance(age, int))       # True
print(isinstance(age, float))     # False
```
`isinstance(value, type)` is preferred over `type(value) == type` because it
handles subclasses.

*Converting types (casting)*
```python
# str to int
age_text: str = "25"
age: int = int(age_text)

# str to float
prict_text: str = "19.99"
price: float = float(price_text)

# number to str
score: int = 100
score_text: str = str(score)

# float to int (truncates, does not round)
pi: float = 3.141592653589793
pi_int: int = int(pi)       # 3

# anything to bool
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False
print(bool("hi"))       # True
print(bool(None))       # False
```
*_Important:_* `int("3.5")` will crash. You must convert to `float` first.
```python
text: str = "3.5"
number: float = float(text)
print(number)       # 3.5
```
##5. Multiple assignment and swapping
```python
x: int = 1
y: int = 2

# swap without a temporary variable
x, y = y, x
print(x, y)     # 2 1

# multiple assignment
a: int
b: int
a, b = 10, 20

# You can also chain variables but this is rarely used and can confuse type
checkers. Prefer one per line.
a: int = b: int = c: int = 0
```

##6. Constants
Python has no true constants. By convention, user *UPPER_SNAKE_CASE*:
```python
PI: float = 3.14159
MAX_USERS: int = 100
DATABASE_URL: str = "postgres://localhost"
```
This tells other developer: Do not change this.

##7. Why, Where and When to use each type
| Type | Why | Where | When |
|------|-----|-------|------|
| `int` | Exact whole numbers | Counts, indexes, IDs, ages | When you need no
decimals|
| `float` | Decimal measurements | Science, temperature, ratios | When precision
is acceptable |
| `str` | Text | Names, messages, files, URLs | Any text data |
| `bool` | Truth values | Conditions, flags | Yes / No, on / off |
| `None` | Absence of value | Optional returns, defaults | When no value makes
sense |

Decision guide:
- Money? Use `Decimal`, not `float`.
- Counting things? Use `int`.
- Measuring thins? Use `float`.
- Text? Use `str`.
- Yes/No? Use `bool`.
- No value yet? Use `None`.

##8. Real-life examples
*Example 1: User profile*
```python
username: str = "chinedum_odili"
age: int = 10
height_m: float = 1.75
is_verified: bool = True
middle_name: str | None = None

print(f"{username} is {age} years old, {height_m}m tall.")
prnt(f"Verified: {is_verified}")
print(f"Middle name: {middle_name}")
```
*Example 2: Shopping cart*
```python
item_name: str = "Rice"
quantity: int = 3
unit_price: float = 12.50
total: float = quantity * unit_price

print(f"{quantity} x {item_name} = {total:.2f}")
```
The `:.2f` inside the f-string means "show 2 decimal places".

*Example 3: Login check*
```python
enter_password: str = input("Password: ")
correct_password: str = "secret123"
is_correct: bool = entered_password == correct_password

print(f"Access granted: {is_correct}")
```
*Example 4: Safe conversion*
```python
age_text: str = input("Age: ")
if age_text.isdigit():
    age: int = int(age_text)
    print(f"Next year you will be {age + 1}")
else:
    print("Pleae enter a whole number")
```
The `.isdigit()` returns a `bool`. We will convert string methods later.

##9. Common mistakes
1. Forgetting quotes around strings: `name = Chinedum` -> `NameError`.
2. Using `True` / `False` with wrong capitalization: `true`, `false` are not
   Python.
3. Assuming `float` math is exact.
4. Using `int("3.5")` and getting a `ValueError`.
5. Confusing `=` (assignment) with `==` (comparison).
6. Reassigning a variable to a different type when hints say otherwise
7. using `type(x) == int` instead of `isinstance(x, int)`.
8. Using `None` in math: `None + 1` crashes.
9. using a mutable default like `[]` in function arguments (we will cover this
   later).
10. Naming a varible `list`, `str`, `int`, `type` - this shadows built-ins.

Bad:
```python
list: list[int] = [1, 2, 3]    # shadows built-in list
```

Good:
```python
numbers: list[int] = [1, 2, 3]
```

##10. Quiz
1. What type is `3.0`?
2. What does `bool("")` return?
3. What does `int(3.9)` return?
4. Why does `0.1 + 0.2` not equals 0.3 exactly?
5. What is the type of `None`?
6. Which is preferred: `type(x) == int` or `isinstance(x, int)`?
7. What naming convention do we use for constants?
8. What does `str | None` mean?
9. What is wrong with `int("3.5")`?
10. True or False: Does Python enforces type hints at runtime?

##11. Test / Exercise for Variables and Data Types
Write a program that:
1. Asks for a product name (`str`).
2. Asks for the quantity (`int`).
3. Asks for the unit price (`float`).
4. Calculates the total.
5. Prints a receipt line using an f-string with 2 decimal places.
6. Uses type hints on every variable.
7. Includes a constant `TAX_RATE: float = 0.15`.
8. Calculate tax and final total
9. Bonus: Put the calculation inside a function with type hinds.
*Example output:*
```text
Product: Rice
Quantity: 3
Unit price: 12.50
Subtotal: 37.50
Tax (15%): 5.63
Total: 43.13
```

##12. Quiz answers
1. `float`
2. `false`
3. `3` - `int()` truncates toward zero, it does not round.
4. Floating point cannot represent `0.1`, `0.2`, or `0.3` exactly in binary
5. `NoneType`.
6. `isinstance(x, int)`.
7. `UPPER_SNAKE_CASE`.
8. A string or `None` - an optional string.
9. It raises `ValueError`. Convert to `flaot` first.
10. False. Hints are not enforced at runtime.

