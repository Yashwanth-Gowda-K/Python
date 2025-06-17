def display_menu():
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent (Power)")
    print("6. Modulus (Remainder)")
    print("7. Exit")

def perform_operation(option , num1 , num2):
    if option == '1':
        return num1 + num1
    elif option =='2':
        return num1 - num2
    elif option =='3':
        return num1 * num2
    elif option =='4':
        if num2 !=0:

            return num1 /  num2
        else:
            return "Error! Division by Zero."
    elif option =='5':
        return num1 ** num2
    elif option == '6':
        if num2 != 0:
            return num1 % num2
    else:
        return "Error! Modulas By zero"
    
while True:
    display_menu()
    user_choice = input("Select an operation(1-7): ")

    if user_choice == '7':
        print("Exiting the calaculator. Goodbye! ")
        break
    if user_choice in ['1', '2', '3', '4', '5', '6']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the sceond number: "))
        except ValueError:
            print("Invalid input! please enter numeric values.")
            continue
        result = perform_operation(user_choice , num1 , num2)
        print(f"The result is: {result}")
    else:
        print("Invalid option. please select a valid operation(1-7)")
