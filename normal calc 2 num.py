num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a  = input("Enter the operator (+, -, *, /): ")
if a == "+":
    result = num1 + num2
elif a == "-":
    result = num1 - num2
elif a == "*":
    result = num1 * num2
elif a == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
else:
    print("Error: Invalid operator.")
    exit()
print("The result is:", result)