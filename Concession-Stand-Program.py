menu = {
    'Popcorn': 50,
    'Soda': 30,
    'Candy': 20,
    'Nachos': 40,
    'Hotdog': 60
}
cart = []
total = 0

# Display menu
print("--- Menu ---")
for item, price in menu.items():
    print(f"{item:10}: ${price:.2f}")

# Ordering loop
while True:
    food = input("\nSelect an item (or 'q' to quit): ").title()  
    if food == 'Q':
        break
    elif food in menu:
        cart.append(food)
        print(f"{food} added to your cart.")
    else:
        print("Invalid item! Please choose from the menu.")

# Calculate and display order summary
if cart:
    print("\n--- Your Order ---")
    for item in cart:
        print(f"{item:10}: ${menu[item]:.2f}")
        total += menu[item]
    
    print("-" * 20)
    print(f"Total: ${total:.2f}")
else:
    print("\nYou didn't order anything.")
