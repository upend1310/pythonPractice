num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator!")

# Note: isinstance(num, float) - this can be used to check if the value is float or not
# But since we are already converting the input to float it will throw an error when not a number
