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

# Part 1: Addition and Subtraction

# Display a header for Part 1
print("########################################")
print("#    Addition and Subtraction          #")
print("########################################")

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate addition and subtraction
sum = num1 + num2
difference = num1 - num2

# Display the results
print("The sum of the two numbers is:", sum)
print("The difference of the two numbers is:", difference)
