# Simple Calculator

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user choice
choice = input("Enter the number of the operation (1/2/3/4): ")

# Perform the calculation
if choice == '1':
    result = num1 + num2
    operation = '+'
elif choice == '2':
    result = num1 - num2
    operation = '-'
elif choice == '3':
    result = num1 * num2
    operation = '*'
elif choice == '4':
    if num2 == 0:
        result = "Error! Division by zero."
        operation = '/'
    else:
        result = num1 / num2
        operation = '/'
else:
    result = "Invalid operation selected."
    operation = '?'

# Display the result
if isinstance(result, float) or isinstance(result, int):
    print(f"\nResult: {num1} {operation} {num2} = {result}")
else:
    print(f"\n{result}")
