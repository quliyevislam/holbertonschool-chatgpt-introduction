#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    This function uses recursion to calculate the factorial.
    
    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number n. If n is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of the input number from the command line
f = factorial(int(sys.argv[1]))
print(f)
