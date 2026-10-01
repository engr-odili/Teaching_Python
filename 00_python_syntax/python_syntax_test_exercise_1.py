#!/usr/bin/env python3
"""
Test / Exercise 1 for python syntax
"""
# Type hints are used for code specificity


def calculate_age(birth_year: int, current_year: int) -> int:
    return current_year - birth_year


name: str = input("What is your name? ")
birth_year_text: str = input("What is your birth year? ")
birth_year: int = int(birth_year_text)
current_year: int = 2026
print(f"Hello, {name}! You are about {calculate_age(birth_year, current_year)}"
      f" years old in {current_year}.")



