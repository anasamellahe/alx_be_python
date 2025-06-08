def perform_operation(num1=0.0, num2=0.0, operation=""):
    match operation:
        case "add":
            return num1 + num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Can't divide by 0."
            return num1 / num2
        case "subtract":
            return num1 - num2
        case _:
            print("invalid operation")