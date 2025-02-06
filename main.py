"""
This script calculates the factorial of a number.
"""

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def get_non_negative_integer():
    """
    Prompts the user to enter a non-negative integer.
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please enter a non-negative integer.")
            else:
                return num
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

num = get_non_negative_integer()
print(f"The factorial of {num} is {factorial(num)}")
