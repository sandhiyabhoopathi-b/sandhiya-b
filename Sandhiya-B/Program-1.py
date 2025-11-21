""" Problem-1: Create a small calculator which performs operations such as Addition, Subtraction,
    Multiplication and Division using class.
    Calculator inputs :> 'a', 'b' and 'type of operation'
    Datatype :> 'a' = double, 'b' = double, 'type of operation' = string """

class Calculator:
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation
    def result(self):
        if self.operation == '+':
            print(f"{self.a} + {self.b} = {self.a + self.b}")
        elif self.operation == '-':
            print(f"{self.a} - {self.b} = {self.a - self.b}")
        elif self.operation == '*':
            print(f"{self.a} * {self.b} = {self.a * self.b}")
        elif self.operation == '/':
            print(f"{self.a} / {self.b} = {self.a / self.b}")
        else:
            print("Type vavllid symbols like + , - , * , /")

num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
operation = input("Choose any one symbol + , - , * , / : ")

c1 = Calculator(num1,num2,operation)
c1.result()



