#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Update n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <integer>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please provide an integer as argument.")
        sys.exit(1)
    
    print(factorial(number))
