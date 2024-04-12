"""
This file provides basics calculator functionality.

It includes functions for performing operations like addition,
subtraction, multiplication, and division.
"""

def addition (a, b) -> float :
    """Add a and b and return the resuts"""
    return a + b

def substraction (c, d) -> float :
    """Substract c and d and return the results"""
    return c - d

def division (e, f) -> float :
    """Divide e by f and return the result"""
    try :
        return e / f
    except ZeroDivisionError:
        print("Div by 0 prohibited")
        return None

def multiplication (g, h) -> float :
    """Multiply g with h and return the result"""
    return g * h
