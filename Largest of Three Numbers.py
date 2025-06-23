def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input. Try again.")

def find_largest():
    print("\n" + "=" * 40)
    print("Enter 3 numbers to find the largest".center(40))
    print("=" * 40)

    a = get_valid_number("Enter the 1st number: ")
    b = get_valid_number("Enter the 2nd number: ")
    c = get_valid_number("Enter the 3rd number: ")

    if a >= b and a >= c:
        print(f"{a} is the greatest number.")
    elif b >= a and b >= c:
        print(f"{b} is the greatest number.")
    else:
        print(f"{c} is the greatest number.")

def main():
    while True:
        find_largest()
        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
