"""
This script calculates the factorial of a number.
"""

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    
    Args:
        n (int): A non-negative integer.
        
    Returns:
        int: The factorial of the integer n.
    """
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def get_non_negative_integer():
    """
    Prompts the user to enter a non-negative integer.
    Keeps asking until a valid number is entered.
    
    Returns:
        int: A valid non-negative integer entered by the user.
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

def main():
    """
    Main function to run the factorial calculation.
    """
    num = get_non_negative_integer()
    print(f"The factorial of {num} is {factorial(num)}")

if __name__ == "__main__":
    main()
