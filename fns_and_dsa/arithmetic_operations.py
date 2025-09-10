# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1: First number
        num2: Second number
        operation: 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        The result of the arithmetic operation, or a string error message
        if the operation is invalid or division by zero occurs.
    """
    if not isinstance(operation, str):
        return "Error: Invalid operation."

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

