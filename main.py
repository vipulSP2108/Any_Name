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

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
