operand_1, operand_2 = int(input("Введите операнд А: ")), int(input("Введите операнд В: "))


operation = input("Введите операцию: ")
if operation == "+":
    print(operand_1 + operand_2)
elif operation == "%" or operation == "mod":
    if operand_2 == 0:
        print("Division by zero")
        exit(1)
    print(operand_1 % operand_2)
elif operation == "-":
    print(operand_1 - operand_2)
elif operation == "x" or operation == "*":
    print(operand_1 * operand_2)
elif operation == "/":
    if operand_2 == 0:
        print("Division by zero")
        exit(1)
    print(operand_1 / operand_2)
elif operation == "^":
    print(a ** b)
