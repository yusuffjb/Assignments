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