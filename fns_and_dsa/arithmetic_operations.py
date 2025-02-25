def perform_operation(num1: float, num2: float, operation: str):
    """Performs the given arithmetic operation on two numbers."""
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
