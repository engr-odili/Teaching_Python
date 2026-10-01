#!/usr/bin/env python3
"""A program that prints a receipt"""
product_name: str = input("Enter product name: ")
quantity_txt: str = input("Enter product quantity: ")
unit_price_txt: str = input("Enter product unit price: ")
quantity: int = 0
unit_price: float = 0.0
TAX_RATE: float = 0.15
total: float = 0.0

quantity = int(float(quantity_txt))
unit_price = float(unit_price_txt)

def calculate_total(
    product_name: str,
    quantity: int,
    unit_price: float,
    TAX_RATE:float
) -> None:
    sub_total: float = quantity * unit_price
    tax: float = sub_total * TAX_RATE
    total: float = sub_total + tax
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Unit price: {unit_price}")
    print(f"Subtotal: {sub_total}")
    print(f"Tax (15%): {tax:.2f}")
    print(f"Total: {total:.2f}")

calculate_total(product_name, quantity, unit_price, TAX_RATE)
