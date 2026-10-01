#!/usr/bin/env python3

def calculate(x: float, y: float) -> None:
    print(f"First number: {x}")
    print(f"Second number: {y}")
    print(f"Sum: {x + y}")
    print(f"Differnece: {x - y}")
    print(f"Product: {x * y}")
    print(f"Quotient: {x / y}")
    print(f"Floor quotiente: {x // y}")
    print(f"Remainder: {x % y}")
    print(f"Power: {x ** y}")

    print()
    age: int = int(float(input("Enter your age: ")))
    print(f"Age: {age}")
    print(f"Teenager: {13 <= age <= 19}")
    print()
    word: str = input("Enter a word: ")
    print(f"Word: {word}")
    print(f"Contains 'a': {'a' in word}")

    print()
    c: int = age
    c += 5
    print(f"Augmented assignment operator: {c}")



x: float = float(input("Enter the first number: "))
y: float = float(input("Enter the second number: "))

calculate(x, y)
