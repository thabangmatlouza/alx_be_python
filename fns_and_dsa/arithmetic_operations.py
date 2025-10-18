def perform_operation(num1, num2, operation):

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

