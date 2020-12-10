a, b = int(input("Введите операнд А: ")), int(input("Введите операнд В: "))

operation = input("Введите операцию: ")
if operation == "+":
    print(a + b)
elif operation == "%" or operation == "mod":
    if b == 0:
        print("Division by zero")
        exit(1)
    print(a % b)
elif operation == "-":
    print(a - b)
elif operation == "x" or operation == "*":
    print(a * b)
elif operation == "/":
    if b == 0:
        print("Division by zero")
        exit(1)
    print(a / b)