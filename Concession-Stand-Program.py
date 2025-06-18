menu = {   
    'Popcorn': 50,
    'Soda': 30,
    'Candy': 20,
    'Nachos': 40,
    'Hotdog': 60
    }
cart = []
total = 0

for key , value in menu.items():
    print(f"{key:10}: ${value:.2f}")

    while True:
        food = input("Select an item: ").lower()
        if food =='q':
            break
        elif menu.get(food) is not None:
            cart.append(food)
        
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"total is : ${total:.2f}")
