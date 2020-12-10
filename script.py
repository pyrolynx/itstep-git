a, b = int(input("Введите операнд А: ")), int(input("Введите операнд В: "))

operation = input("Введите операцию: ")
if operation() == "+":
    print(a + b)
elif operation == "%" or operation == "mod":
    print(a % b)
elif operation == "-":
    print(a - b)
elif operation == "x" or operation == "*":
    print(a * b)
