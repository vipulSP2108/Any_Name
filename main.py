import time

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

def calculate_and_display_factorial():
    """
    Calculates and displays the factorial of a number, while showing the time taken for the calculation.
    """
    num = get_non_negative_integer()
    start_time = time.time()  # Record the start time
    result = factorial(num)
    end_time = time.time()  # Record the end time
    print(f"The factorial of {num} is {result}")
    print(f"Time taken to calculate: {end_time - start_time:.6f} seconds")

def main():
    """
    Main function that allows the user to calculate multiple factorials or exit.
    """
    while True:
        calculate_and_display_factorial()
        
        continue_prompt = input("Do you want to calculate another factorial? (y/n): ").strip().lower()

main()
