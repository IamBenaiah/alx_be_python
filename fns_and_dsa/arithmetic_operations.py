# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """Perform basic arithmetic operations based on the given operation."""
    
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        case _:
            return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."
