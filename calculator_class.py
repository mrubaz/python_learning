class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero is not allowed."
        return self.num1 / self.num2


# Example usage
if __name__ == "__main__":
    # User input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Press 1 for Add")
    print("Press 2 for Subtract")
    print("Press 3 for Multiply")
    print("Press 4 for Divide")
    operation = input("Choose operation: ")

    # Create calculator object
    calc = Calculator(num1, num2)

    # Perform operation
    if operation == "1":
        print("Result:", calc.add())
    elif operation == "2":
        print("Result:", calc.subtract())
    elif operation == "3":
        print("Result:", calc.multiply())
    elif operation == "4":
        print("Result:", calc.divide())
    else:
        print("Invalid operation selected.")
