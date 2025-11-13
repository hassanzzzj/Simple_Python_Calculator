num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

if operation == "1":
    result = num1 + num2
    print("Result:", result)
elif operation == "2":
    result = num1 - num2
    print("Result:", result)
elif operation == "3":
    result = num1 * num2
    print("Result:", result)
elif operation == "4":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operation choice.")
