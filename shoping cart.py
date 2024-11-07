shopping_cart = []

def view_cart():
    if not shopping_cart:
        print("Your cart is empty..")
    else:
        print("Items in cart:")
        for index , item in enumerate(shopping_cart , start=1):
            print(f"{index} . {item}")

def add_item():
    item = input("Enter the item to add to cart.")
    shopping_cart.append(item)
    print(f"{item} has been added to your cart.")


def remove_item():
    view_cart()
    try:
        item_number = int(input("Enter the item number to remove: ")) -1
        if 0<= item_number <len(shopping_cart):
            remove_item = shopping_cart.pop(item_number)
            print(f"{remove_item} has been removed from your cart.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_cart():
    shopping_cart.clear()
    print("Your cart has been cleared.")

def main():
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Clear Cart")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            view_cart()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            clear_cart()
        elif choice == '5':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


main()

        