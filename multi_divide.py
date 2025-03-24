# ASCII art banner
print(r"""
   _____________________
  |  _________________  |
  | | Python Calc   0.| |
  | |_________________| |
  |  ___ ___ ___   ___  |
  | | 7 | 8 | 9 | | + | |
  | |___|___|___| |___| |
  | | 4 | 5 | 6 | | - | |
  | |___|___|___| |___| |
  | | 1 | 2 | 3 | | * | |
  | |___|___|___| |___| |
  | | . | 0 | = | | / | |
  | |___|___|___| |___| |
  |_____________________|
""")

# Part 2: Multiplication and Division

# Display a header for Part 2
print("########################################")
print("#  Multiplication and Division         #")
print("########################################")

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate multiplication
product = num1 * num2

# Calculate division with a check for division by zero
if num2 != 0:
    quotient = num1 / num2
    print("The quotient of the two numbers is:", quotient)
else:
    print("Division by zero is not allowed.")

# Display the multiplication result
print("The product of the two numbers is:", product)
