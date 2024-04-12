"""
This file provides test for basics calculator functionality from calculator.

It includes test functions for addition,
subtraction, multiplication, and division.
"""


from calculator import addition, substraction, division, multiplication

def test_addition():
    """Test if addition is working correcty"""
    assert addition(1, 2) == 3

def test_substraction():
    """Test if substraction is working correcty"""
    assert substraction(10, 2) == 8

def test_division():
    """Test if division is working correcty"""
    assert division(26, 2) == 13

def test_division():
    """Test if multiplication is working correcty"""
    assert multiplication(3, 4) == 12
