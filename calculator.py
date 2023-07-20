class Calculator:
    def __init__(self, operation, number1, number2):
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
    def add(self):
        answer = float(self.number1) + float(self.number2)
        print(answer)
    def subtract(self):
        answer = float(self.number1) - float(self.number2)
        print(answer)
    def multiply(self):
        answer = float(self.number1) * float(self.number2)
        print(answer)
    def divide(self):
        answer = float(self.number1) / float(self.number2)
        print(answer)


index  = 1

while index > 0:
    print("Welcome, this is a simple four function calculator.")
    operation = input("What operation would you like to complete(add, subtract, multiply, divide)?")
    number1 =float(input("What is the first number?"))
    number2 = float(input("What is the second number?"))
    calculator = Calculator(operation, number1, number2)

    if operation == "add":
        calculator.add()
        index -= 1
    elif operation == "subtract":
        calculator.subtract()
        index -= 1
    elif operation == "multiply":
        calculator.multiply()
        index -= 1
    elif operation == "divide":
        calculator.divide()
        index -= 1
    if index == 0:
        an = input("Would you like to use this calculator again?")
        if an == "yes":
            index += 1
        else:
            break
