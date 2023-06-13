class Calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num1

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

    def modulo(self, num1, num):
        return num1 % num2

    def res(self):
        print("result:", self.add, self.sub, self.mul, self.div, self.modulo)


while True:
    input_string = input("Enter the input:")
    operands = input_string.split(" ")
    num1 = float(operands[0])
    num2 = float(operands[2])
    operator = operands[1]
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        try:
            print(num1 / num2)

        except:

            print("not possible")
    elif operator == "%":
        print(num1 % num2)
    else:
        print("provide the proper input")
    print()


