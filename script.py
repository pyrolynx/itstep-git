a, b = int(input()), int(input())

operation = input()
if operation() == "+":
    print(a + b)
elif operation == "%" or operation == "mod":
    print(a % b)
elif operation == "-":
    print(a - b)
elif operation == "x" or operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)