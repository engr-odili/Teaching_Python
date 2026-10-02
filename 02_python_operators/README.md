# 002 PYTHON OPERATORS
---
Operators are symbols that perform actions on values. you already met a few in
Basic Syntax. Now we go deep. By the end, you will know every major operator,
when to use them, and the traps that catch beginners.

Every example uses *type hints*, and i explain them as we go.

##1. What is an operator?
An operator takes one or more *operands* (values) and produces a result.
```python
result: int = 10 + 5
```
- `10` and `5` are operands.
- `+` is the operator.
- `result` is the value produced.

Operators are grouped by what they do:
| Group | Example |
|-------|---------|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | `and`, `or`, `not` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` |
| Identity | `is`, `is not` |
| Membership | `in`, `not in`|
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>`, `:=` |

We will cover each as me move forward.

##2. Arithmetic Operators
```python
a: int = 10
b: int = 3

add: int = a + b                            # 13
sub: int = a - b                            # 7
mul: int = a * b                            # 30
div: float = a / b                          # 3.3333333333333335
floor_div: int = a / b                      # 3 (rounds down)
mod: int = a % b                            # 1 (remainder)
power: int = a ** b                         # 1000
```
*_Important Notes_*:
- `/` always returns a float, even if the division is exact: `10 / 2` -> `5.0`
- `//` is *floor division*. It rounds *down*, not toward zero.
```python
print(7 // 2)           # 3
print(-7 // 2)          # -4 (not -3!)
```
- `%` us tge renaubder, Also called *modulo*
```python
print(10 % 3)           # 1
print(10 % 3)           # 0  (even)
print(11 % 2)           # 1  (odd)
```
Commonuse of `%`: check even or odd.
```python
number: int = 7
is_even: boole = number % 2 == 0
print(is_even)          # False
```
- `**` is exponentiation, not `^`. In Python, `^` is bitwise XOR.
```python
print(2 ** 3)           # 8
print(2 ^ 6)            # 1 (bitwise XOR - not what beginners expect)    
```
*Type hints for arithmetic*
- `int + int` -> `int`
- `int + float` -> `float`
- `int / int` -> `float`
- `int // int` -> `int`
- `int ** int` -> `int` (unless negative exponent -> `float`)

##3. Comparison Operators
Comparison operators return a `bool`.
```python
x: int = 5
y: int = 10

print(x == y)           # False     equal
print(x != y)           # True      not equal
print(x < y)            # True
print(x >)              # False
print(x <= y)           # True
print(x >= y)           # False
```

We can chain comparisons, which is very Pythonic:
```python
age: int = 10
is_young_adult: bool = 18 <= age < 30
print(is_young_adult)   # False
```
This is cleaner than:
```python
is_young_adult: bool = age >= 18 and age < 30
```
Both are correct. Chaining reads better.

*Comparing different types*
```python
print(1 == 1.0)         # True (value comparison)
print(1 is 1.0)         # False (differnt types)
print("1" == 1)         # False (str vs int)
```
*_Careful: Python 3 does not compare `str` and `int` with `<` or `>`_*

```python
`"5" < 10 #TypeError` convert first if needed
```
##4. Logical Operators
Logical operators combine `bool` values.
```python
is_raining: bool = True
has_umbrella: bool = False

print(is_raining and has_umbrella)      # False
print(is_raining or has_umbrella)       # True
print(not is_raining)                   # False
```
*Truth Tables*
`and`:
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

`or`:
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

`not`:
| A | not B |
|---|-------|
| True | False |
| False | True |

*Short-circuit evaluation*
Python stops evaluating as soon as the result is known.
```python
def is_adult(age: int) -> bool:
    print("checking age")
    return age >= 18

# age is 15, so first check fails, second not evaluated.
result: bool = is_adult(15) and is_adult(20)
```
Output: only one "checking age"

This matters when the second check would crash:
```python
names: list[str] = []
# safe: len(names) > 0 is False, so name[0] is never evaluated.
if len(names) > 0 and names[0] == "Chinedum":
    print("found")
```

*Truthy and falsy values*
`and`, `or`, `not` work on any value, not just `bool`.

Falsy values:
- `False`
- `0`, `0.0`
- `""` (empty string)
- `[]`, `()`, `{}`, `set()` (empty collections)
- `None`

Everythin else is truthy.
```python
print(bool(0))              # False
print(bool(""))             # False
print(bool([]))             # False
print(bool(None))           # False
print(bool("hi"))           # True
print(bool([0]))            # True (non-empty list)
```

`and` and `or` return the actual operand, not just `True` / `False`
```python
name: str = "" or "Guest"
print(name)                 # Guest

value: int = 5 and 10
print(value)                # 10
```
This is used for defaults, but be careful.

Prefer:
```python
name: str = input_name if input_name else "Guest"
```
We will cover this in conditionals

##5. Assignment operators
Basic assignment:
```python
x: int = 10
```
Augmented assignment combines an operation with assignment:
```python
x: int = 10
x += 5              # x = x + 5 -> 15
x -= 3              # x = x - 3 -> 12
x *= 2              # x = x * 2 -> 24
x /= 4              # x = x / 4 -> 6.0  (float)
x //= 2             # x = x // 2 -> 3.0
x %= 2              # x = x % 2 -> 1.0
x **= 2             # x = x ** 2 -> 1.0
```
Note: `x /= 4` changes `x` to `float`. Type hints do not stop this.

Augmented assignment works on strings and list too.
```python
message: str = "Hello"
message += " World"
print(message)              # Hello World

numbers: list[int] = [1, 2]
numbers += [3, 4]
print(numbers)              # [1, 2, 3, 4]
```

##6. Identity operators: `is` and `is not`
`is` checks whether two names point to the *same object* in memory, not whether
values are equal.
```python
a: list[int] = [1, 2, 3]
b: list[int] = [1, 2, 3]
c: list[int] = a

print(a == b)       # True (same values)
print(a is b)       # False (different objects)
prnt(a is c)        # True (same object)
```
Use `is` only for:
- `None`: `if value is None:`
- `True` / `False`: rarely needed, just use `if flag:`
- Sentinel objects (advanced)

Never use `is` to compare numbers or strings:
```python
x: int = 1000
y: int = 1000
print(x is y)       # may be True or False depending on Python's caching
```

Use `==` for values.

Bad:
```python
if name is "Chinedum":               # wrong
    ...
```
Good:
```python
if name == "Chinedum":
    ...
```

##7. Membership operators: `in` and `not in`
Check if a value exists in a sequence.
```python
fruits: list[str] = ["apple", "banana", "cherry"]
print("banana" in fruits)                   # True
print("mango" not in fruits)                # True
name: str = "Odili Chinedum Christian"
print("Chinedum" in name)                   # True
grades: dict[str, int] = {
"math": 90,
"science": 85
}
print("math" in grades)                     # True (checks keys)
```
`in` works on lists, tuples, strings, dicts (keys), and sets.

##8. Bitwise operators
Bitwise operators work on the binary representatin of integers. Most beginners
rarely need them, but you should recognise them.
```python
a: int = 5              # binary 0101
b: int = 3              # binary 0011

print(a & b)            # 1 AND
print(a | b)            # 7 OR
print(a ^ b)            # 6 XOR
print(~a)               # -6 NOT
print(a << 1)           # 10 left shift (multiply by 2)
print(a >> 1)           # 2 righ shift (divide by 2)
```
When use them:
- Flags and permission (combine many yes/no options into one number)
- Low-level work: networking, cryptography, graphics.

Where:
Rarely in everyday scripts.

When:
When you need compact flags or performance.

*Example: permission flags:*
```python
READ: int = 0b001       # 1
WRITE: int = 0b010      # 2
EXECUTE: int = 0b100    #4

permissions: int = READ | WRITE   # 3

can_read: bool = bool(permission & READ)   # True
can_execute: bool = bool(permission & EXECUTE)    # False
```

##9. The Walrus Operator `:=`
Introduced in Python 3.8. it assigns a value and returns it in one expression.

Without walrus:
```python
data: str = input("Enger something: ")
if len(data) > 0:
    print(f"Got: {data}")
```

With Walrus:
```python
if (data := input("Enter something: ")):
    print(f"Got: {data}")
```

Why use it:
- Avoid calling the same function twice.
- Keep code shorter when the value is used immediately.

Where:
Inside `if`, `while`, and comprehensions.

When:
Only when it improves readability. Do not overuse it.

Example with `while`:
```python
line: str = ""
while(line := input("Type something (or 'quit'): ")) != 'quit':
    print(f"You typed: {line}")
```

##10. Operator precedence

Python evaluates operators in this order (highest to lowest, simplified):
1. `**`
2. `+x`, `-x`, `~x`  (unary)
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `<<`, `>>`
6. `&`
7. `^`
8. `|`
9. Comparisons (`==`, `<`, `>`, etc).
10. `not`
11. `and`
12. `or`
13. `:=`

When in doubt, use parentheses.
```python
result: int = 2 + 3 * 4         # 14, not 20
result2: int = (2 + 3) * 4      # 20
```

##11. Why, Where, and When to use each

| Operator | Why | Where | When |
|----------|-----|-------|------|
| `+ - * /` | Basic math | Everywhere | Almost always |
| `//` | Whole-number division | Indexing, grouping | When you need an `int` |
| `%` | Remainder | Even / Odd, Cycles, time | When you need the remainder |
| `**` | Power | Math, science | When squaring or exponentiating |
| `== != < >` | Compare values | Conditions | When comparing |
| `and or not` | Combine conditions | Conditions | When multiple checks needed |
| `+= -=` etc. | Shorten updates | Counters, totals | When updating a variable |
| `is` | Same object | `None` checks | Only for `None` and sentinels
| `in` | Membership | List, strings, dicts | When checking existence |
| Bitwise | Compact flags | Low-level code | Rarely, for permissions. |
| `:=` | Assign in expression | `if`, `while` | When it reduces repetition |

##12. Real-life examples
*Example 1: Even or odd*
```python
number: int = int(input("Enter a number: "))
is_even: bool = number % 2 == 0
print(f"{number} is {'even' if is_even else 'odd'}")
```

*Example 2: Discount checker*
```python
price: float = 250.0
is_member: bool = True
has_coupon: bool = False

gets_discount: bool = is_member or has_coupon
final_price: float = price * 0.9 if gets_discount else price
print(f"Final price: {final_price:.2f}")
```

*Example 3: Login Validation*
```python
username: str = input("Username: ")
password: str = input("Password: ")

is_valid: bool = (
    len(username) >= 3
    and len(password) >= 8
    and username != password
)
print(f"Valid: {is_valid}")
```

*Example 4: Age range check*
```python
age: int = int(input("Age: "))
is_teenager: bool = 13 <= age <= 19
is_senior: bool = age >= 65
print(f"Teenager: {is_teenager}, Senior: {is_senior}")
```

*Example 5: Function with type hints*
```python
def appy_tax(amount: float, rate: float) -> float:
"""Return amount with tax applied."""
return amount * (1 + rate)
sub_total: float = 100.00
total: float = apply_tax(sub_total, 0.15)
print(f"Total: {total:.2f}")
```

##13. Common mistakes
1. Using `=` instead of `==` in comparisons.
2. Using `^` for power instead of `**`
3. Expecting `/` to return an `int`
4. Forgetting that `//` rounds down, not towards zero.
5. Using `is` to compare values instead of `==`.
6. Comparing `str` and `int` directly with `<` or `>`.
7. Ignoring operator precedence.
8. Overusing the walrus operator and hurting readability.
9. Assuming `and` / `or` return only `True` or `False`.
10. Using `&` / `|` when you meant `and` / `or`

Bad:
```python
if age > 18 & has_id:       # & is bitwise, not logical
    ...
```

Good:
```python
if age > 18 and has_id:
    ...
```

##14. Quiz
1. What does `10 / 2` return, and what type?
2. What does `-7 // 2` return?
3. What does `10 % 3` return?
4. What does `2 ** 3` return?
5. What does `2 ^ 3` return?
6. What is the difference between `==` and `is`?
7. What does `bool([])` return?
8. What does `"" or "Guest"` return?
9. What does `5 and 10` return?
10. Which operator checks membership?
11. what does `18 <= age < 30` mean?
12. What does `x := 5` do?
13. What does `~5` return?
14. Why is `"5" < 10` a `TypeError`?
15. What is the result of `2 + 3 * 4`?

##15. Test / Exercise
Write a program that:
1. Asks the user for two numbers (`float`).
2. Prints the sum, difference, product, quotiente, floor quotient, remainder,
   and power.
3. Uses type hints on every variable.
4. Asks for the user's age and checks if they are teenager(13 - 19).
5. Asks for word and checks if the letter `"a"` is in it.
6. Uses at least one augmented assignment operator.
7. Uses at least one logical operator.
8. Bonus: put the arithmetic in function `calculate(x: float, y: float) -> None`
   that prints all results.

Example output:
```text
First number: 10
Second number: 3
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.33333333333333335
Floor quotiente: 3.0
Remainder: 1.0
Power: 1000.0

Age: 15
Teenager: True

Word: banana
Contains 'a': True
```

##16. Quiz answers
1. `5.0`, type `float`.
2. `-4` - floor division rounds down.
3. `1`.
4. `8`.
5. `1` - `^` is bitwise XOR.
6. `==` compares values; `is` checks identity (same object).
7. `False` - empty list is falsy.
8. `"Guest"`.
9. `10` - `and` returns the second operand if the first is truthy
10. `in` (and `not in`).
11. `age` is between 18 and 29 inclusive.
12. Assigns `5` to `x` and returns `5` as and expression.
13. `-6` - bitwise NOT.
14. Python 3 does not allow ordering comparisons between `str` and `int`.
15. `14` - multiplication before addition.

#BONUS ADVANCED TOPIC
##THE PYTHON `@` (Matrix Multiplication) Operator
This is a fascinating topic. The `@` symbol in Python has *two completely
differnt meanings* depending on where it appears:
1. As a *decorator* - `@my_decorator` on its own line above a function
2. As the *matrix multiplication operator* - `a @ b` between two value.

We are covering meaning #2 here. Meaning #1(decorators) is a separate advanced
topic we will do later. Do not confuse them.

Every example uses *type hints*, explained as we go.

##1. What is the matrix multiplication operator?
The `@` operator performs *matrix multiplication* (also called the matrix
product). It was added in Python 3.5 (PEP 465) specifically because the `*`
opertor was already used for element-wise multiplication in libraries like
NumPy, and mathematicians neede a distinct symbol.
```python
result: Matrix = a @ b          # matrix multiplication
result2: Matrix = a * b         # element-wise multiplication (in Numpy)
```
Mathematically, if `A` is an `m x x` matrix and `B` is an `n x p` matrix, then
`A @ B` produces an `m x p` matrix.

##2. Why does`@` exist?
Before Python 3.5, if you wanted matrix multiplication in Numpy, you had to
write:
```python
result = np.dot(a, b)

# or

result = a.dot(b)
```
This was ugly and did not read like math. The `*` operator was already taken for
element-wise multiplication. So Python introduced `@` as a dedicated operator
for matrix multiplication.

Why it matters:
- Readability: `C = A @ B` looks like linear algebra.
- Consistency: libraries can implement it uniformly.
- Customisation: you can define `@` for your own class.

Where it is used:
- NumPy, PyTouch, TensorFlow, JAX - machine learning and scientific computing.
- Linear algebra libraries.
- Custom matrix/vector classes.

When to use it:
- When working with matrices or vectors that support it.
- Almost never in Python lists - it will raise `TypeError`.

##3. The `@` operator does not work on built-in lists
This surprises beginners. The `@` operator is *not* built into Python's core
types.
```python
a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]
# result = a @ b    # TypeError: unsupported oerand type(s) for @: 'list' and
'list'
```
You must use a library like NumPy, or implement `__matmul__` yourself.

##4. How `@` works: the dunder methods
when Python sees `a @ b`, it looks for the method `__matmul__` on `a`'s calass.
If not fount, it tries `__rmatmul__` on `b`. For `a @= b`, it tires `__imatmul__`.

| Operator | Method | Called on |
|----------|--------|-----------|
| `a @ b` | `__matmul__(self, other)` | type of `a` |
| `a @ b` (fallback) | `__rmatmul__(self, other)` | type of `b` |
| `a @ b` | `__imatmul__(self, other)` | type of `a` |

These are *dunder methods* (double underscore). We will cover them deeply later,
but here is the idea: Python translates operators into methods calls.
Example: `a + b` becomes `a.__add__(b)`.
so `a @ b` becomes `a.__matmul__(b)`.

##5. Using `@` with NumPy (the most common real use)
NumPy is the standard library for numerical computing. Install it first:
```bash
pip install numpy
```
Then:
```python
import numpy as np
from numpy.typing import NDArray

# 2x2 matrices
A: NDArray[np.float64] = np.array([[1, 2], [3, 4]], dtype=np.flaot64)
B: NDArray[np.float64] = np.array([[5, 6], [7, 8]], dtype=np.flaot64)

C: NDArray[np.float64] = A @ B
print(C)
# [[19 22]
#  [43 50]]
```

Compare with element-wise `*`:
```python
element_wise: NDArray[np.float64] = A * B
print(element_wise)

# [[5 12]
#  [21 32]]
```
They are completely different operations.
This is exactly why `@` was introduced.

