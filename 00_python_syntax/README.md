# PYTHON BASIC SYNTAX
---
Welcome to your first lesson.
*Basic syntas* is the grammar of Python. It is how you write code so Python can
understand it. Just as English has rules for capitalization, punctuation, and
sentence structure so that humans can understand each other, Python has syntax
rules so that the computer can unserstand your instructions.
If you break syntax rules, Python raises a `SyntaxError.`

I'll explain everything from zero, and every example that uses variables or
functions will include *type hints.*

##1. Your first Python program
```python
print("Hello, world!")
```
What is happening:
- `print` is a built-in function. it displays something on the screen.
- `"Hello, world!"` is a *string*. A string is text inside quotes.
- Parentheses `()` hold the value you want to print.

You can run this by saving it in a file called `hello.py` and running:
```python
python hello.py
```
##2. Statements and lines
A *statement* is one instruction. Usually, one statement per line.
```python
print("Welcome")
print("To Python")
```
You don *not* need semicolons at the end of lines. This works, but it is not
*Pythonic.*
```python
print("Hello"); print("world")
```
Python Prefer:
```python
print("Hello")
print("World")
```

If a line is too long, you can continue it inside parentheses:
```python
total: int = (
    10
    + 20
    + 30
    + 40
    + 50
)
print(total)
```

##3. Comments
A comment is ignored by Python. Use `#`.
```python
# This is a comment
name: str = "Chinedum" # This is also a comment
```
Use comments to explain *why*, not *what*.

Bad comment:
```python
# Add 1 to age
age: int = age + 1
```

Better comment:
```python
# The system stores age in full years, so we round up after birthday
age: int = age + 1
```

Triple quotes are often used for documentation, not comments:
```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
```
Technically this is a *docstring*, not a comment. We will cover functions later,
but notice the type hints.

##4. Indentation matters
Python uses *indentation* to define blocks of code. Most languages use `{}`.
Python uses spaces.

The standard is *4 spaces*
```python
is_raining: bool = True
if is_raining:
    print("Take an umbrella")
else:
    print("No umbrella needed")
```

Notice:
- `if is_raining:` ends with a colon `:`.
- The indented line under it belongs to the `if`.
- The `else:` line is not indented inside the `if` but it share same
    indentation line with the `if is_raining:`.
- The line under `else:` is indented.

If indentation is wrong, you get `IndentationError`.

*Common mistakes:*
```python
if is_raining:
print("Take an umbrella") # wrong: missing indentation
```

*Correct*
```python
if is_raining:
    print("Take an umbrella")
```

##5. Variables and type hints:
A variable is a name that stores a value.

```python
name: str = "Chinedum"
age: int = 10
height: float = 1.75
is_student: bool = True
```

The pattern is:
```text
variable_name: type = value
```
Examples:
- `name: str = "Chinedum"`    # means `name` should be a string.
- `age: int = 10`             # means `age` should be an integer.
- `height: float = 1.75`      # means `height` should be a decimal number
- `is_student: bool = True`   # means `is_student` should be a boolean value (True or False)
_*Important:* Python does *not* enforce type hints at runtime._ This still runs:
```python
age: int = "Ten"
```
But tools like `mypy` will warn you, and your code becomes harder to trust. Use
type hints to make your intention clear.

You can check a value's type with `type()`:
```python
age: int = 10
print(type(age))   # <class 'int'>
```
*Variable naming rules*
- Can contain letters, numbers, and underscores.
- Cannot start with a number
- Case-sensitive: `age` and `Age` are different.
- Cannot be a Python keyword like `if`, `else`, `for`, `class`, `def`.
- Use `snake_case` for normal variables.

Good:
```python
first_name: str = "Chinedum"
total_price: float = 99.99
```

Bad:
```python
2name: str = "Chinedum"             # cannot start with number
first-name: str = "Chinedum"        # hyphen is not allowed
class: str ="Math"                  # calss is a keyword
```

##6. Input and output
Output uses `print()`.
```python
name: str = "Chinedum"
print(f"Hello, {name}!")
```

The `f` before the string means *f-string*. It lets you put variables inside `{}`.

input uses `input()`.
```python
name: str = input("What is your name? ")
print(f"Hello, {name}!")
```
_*Important:* `input()` always returns a *string*, even if the user types in a
number._
```python
age_text: str = input("How old are you? ")
print(f"input returns a {type(age_text)} type for age_text")
age: int = int(age_text)
print(f"age_text was converted to {type(age)} by explicitly casting it with "
      f"int(age_text)")
```
Here:
- `age_txt` is a string.
- `int(age_text)` converts it to an integer.
- `age: int` stores the integer.

If the user types something that is not a number, `int()` will crash. We will
learn error handling later.

##7. Basic operators you will see
We will cover operators deeply later, but you need a few now.

*Arithmetic:*
```python
a: int = 10
b: int = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3      floor division
print(a % b)    # 1      remainder
print(a ** b)   # 1000   power

*Comparison:*
```python
x: int = 5
y: int = 10

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
```

*Logical*
```python
is_running: bool = True
has_umbrella: bool = False

print(is_raining and has_umbrealla)        # False
print(is_raining or has_umbrella)          # True
print(not is_raining)                      # False
```

##8. Why, where, and when to use what
*Indentation*
- *Why:* Python uses it to know which lines belong together.
- *Where:* Every block: `if`, `else`, `for`, `while`, `def`, `class`.
- *When:* Always. Use 4 spaces. Do not mix tabs and spaces.

*Comments*
- *Why:* To explain why code exists, not what it does. 
- *Where:* Above complex logic, or next to surprising decisions.
- *When:* When the code is not obvious. Do not comment everyline.

*Type hints*
- *Why:* To make code readable and catch mistakes with tools.
- *Where:* Function parameters, function return values, and variables when the
    type is not obvious.
- *When:* In professional code, almost always for functions. For simple local
    variables, use them when it improves clarity

*`print()`*
- *Why:* To show output or debug
- *Where:* Scripts, learning, debugging.
- *When:* When you need to display information

*`input()`*
- *Why:* To get data from the user.
- *Where:* Interactive scripts and small programs.
- *When:* When the program needs user input. Remember to convert it if you need
    a number.
##9. Real-life examples
*Example 1: Greeting program*
```python
name: str = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python.")
```
*Example 2: Age calculator*
```python
name: str = input("What is your name? ")
birty_year_text: str = input("What year were you born? ")
birth_year: int = int(birth_year_text)
current_year: int = 2026
age: int = current_year - birth_year
print(f"Hello, {name}! You are about {age} years old in {current_year}.")
```
*Example 3: Temperature converter*
```python
celsius_text: str = input("Temperature in Celsius: ")
celsius: float = float(celsius_text)
fahrenheit: float = (celsius * (9/5)) + 32
print(f"{celsius}C is {fahrenheit}F")
```
*Example 4: Simple function with type hints*
```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")
user_name: str = input("Enter your name: ")
greet(user_name)
```
`-> None` means the function returns nothing. It only performs an action.

##10. Common mistakes
1. Missing colon after `if`, `else`, `for`, `while`, `def`.
2. Wrong indentation.
3. Usin `=` instead of `==` in comparisons.
4. Forgetting quotes around strings.
5. Forgetting to convert `input()` to `int` or `float`.
6. Starting a variable name with a number.
7. Using a Python keyword as a variable name
8. Mixing tabs and spaces.
9. Thinking type hints enforce types at runtime. They do not.
10. Writing comments that explain what instead of why.

##11. Quiz
Try these before looking at the answers.
1. What is wrong with this line?
```python
if age > 18
    print("Adult") 
```
2. Which variable name is valid?
```text
2name
my_name
my-name
class
```
3. What type does `input()` return?
4. What does `-> None` mean in this function?
```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")
```
5. True or False: Python uses `{}` to define blocks.
6. What symbol starts a single-line comment?
7. What type hint would you use for `prince = 19.99` ?
8. Fix the indentation:
```python
is_hungry: bool = True
if is_hungry:
print("Eat something")
```

##12. Test / Exercise for python syntax
*Exercise 1*
Write a python program that:
1. Asks the user for their name.
2. Asks the user for their birth year.
3. Converts the birth year to an integer.
4. Calculate their age in 2026.
5. Prints a greeting with their name and age
6. Uses type hints for all variables.
7. Includes at least one comment explaining why something is done.
8. Bonus: Put the age calculation inside a function with type hints.
*Example Output*
```text
What is your name? Chinedum
What year where you born? 2006
Hello, Chinedum! You are about 20 years old in 2026
```
*Exercise 2*
1. Create a function called `create_profile` that returns nothing
2. Inside the function, add a docstring explaining what it does.
3. Create three variables with *strict type hints*:
- A string for a `city`
- An integer for a `zip_code`
- A boolean for `is_coastal`
4. Use `print()` and an *f-string* to output a sentence combining all three
   variables.
5. Call the function outside of the function block (un-indented).

##13. Quiz answers
1. Missing colon after `if age > 18:`.
2. `my_name` is valid.
3. `input()` returns a string
4. `-> None` means the function returns nothing. It only prints.
5. False. Python uses indentation
6. `#`
7. `float`
8. Correct:
```python
is_hungry: bool = True
if is_hungry:
    print("Eat something")
```

