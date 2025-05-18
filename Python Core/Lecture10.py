# Mini Calculator (Using Functions & OOP)
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."


# User interaction
def main():
    calc = Calculator()
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", calc.add(a, b))
    elif op == '-':
        print("Result:", calc.subtract(a, b))
    elif op == '*':
        print("Result:", calc.multiply(a, b))
    elif op == '/':
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()
