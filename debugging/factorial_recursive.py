#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Args:
        n (int): The number to calculate the factorial for. Must be a non-negative integer.

    Returns:
        int: The factorial of the given number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    """
    Main entry point of the script. Reads a number from the command-line arguments,
    calculates its factorial, and prints the result.
    """
    try:
        # Convert the first command-line argument to an integer
        number = int(sys.argv[1])
        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            # Calculate and print the factorial
            result = factorial(number)
            print(result)
    except (IndexError, ValueError):
        print("Usage: ./factorial_recursive.py <non-negative integer>")