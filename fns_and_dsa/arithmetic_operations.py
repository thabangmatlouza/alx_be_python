"""
arithmetic_operations.py

Provides a single function `perform_operation` which performs basic arithmetic
operations: add, subtract, multiply, divide.
"""
from typing import Union

def perform_operation(num1: float, num2: float, operation: str) -> Union[float, str]:
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float | str: The operation result, or an error message string for
                     division by zero or invalid operations.
    """
    if not isinstance(operation, str):
        return "Error: Invalid operation."

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    if op == "subtract":
        return num1 - num2
    if op == "multiply":
        return num1 * num2
    if op == "divide":
        # handle division by zero explicitly
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    return "Error: Invalid operation."
