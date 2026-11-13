import math
#PART A
# Simple Calculator
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Performing calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
# Displaying results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")

#PART B
print("\n=== Area Calculations ===")
# 1. Area of a Rectangle
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
area_rectangle = length * width
print(f"Area of Rectangle: {area_rectangle:.2f}")

# 2. Area of a Circle
radius = float(input("Enter circle radius: "))
area_circle = math.pi * (radius ** 2)
print(f"Area of Circle: {area_circle:.2f}”)
