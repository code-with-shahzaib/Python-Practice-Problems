"""
6. Write a python program to calculate the square of a number entered by the user.
"""

number = int(input("Enter Number Which Square you Want: "))

# square = number * number
square = number ** 2 # This is more Pythonic Way to Find Sqaure

print(f"The Sqaure of {number} = {square}")