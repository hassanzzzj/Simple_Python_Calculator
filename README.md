

````
# Simple Python Calculator

A basic command-line calculator program written in Python. This script allows users to perform fundamental arithmetic operations (addition, subtraction, multiplication, and division) on two numbers.

## ✨ Features

* **Four Basic Operations:** Supports `+`, `-`, `*`, and `/`.
* **Input Validation:** Includes a check to prevent **division by zero** errors.
* **User-Friendly Interface:** Simple text prompts guide the user through the input process.

## 🚀 Getting Started

### Prerequisites

You need **Python 3** installed on your system.

### Installation and Execution

1.  **Save the Code:** Save the provided code into a file named, for example, `calculator.py`.

2.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the following command:

    ```bash
    python calculator.py
    ```

3.  **Follow the Prompts:** The program will prompt you to:
    * Enter the first number.
    * Enter the second number.
    * Choose the operation (1 for +, 2 for -, 3 for *, 4 for /).

## 💻 Code Example

Here is the source code:

```python
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
````
