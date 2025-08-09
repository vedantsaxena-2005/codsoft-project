def calculator():
    print("=== Simple Calculator ===")
    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    try:
        # Get user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        choice = input("Enter operation (1/2/3/4): ")

        # Perform calculation
        if choice == '1':
            result = num1 + num2
            operator = '+'
        elif choice == '2':
            result = num1 - num2
            operator = '-'
        elif choice == '3':
            result = num1 * num2
            operator = '*'
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
            operator = '/'
        else:
            print("Invalid operation choice.")
            return

        # Display result
        print(f"\nResult: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
# Run the calculator
calculator()