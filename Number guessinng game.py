import random

def Number_guessing_game():
    numbers = random.randint(1 , 100)
    attempts = 0

    print("Lets play a Number guessing game")

    while True:
        guess = input("Enter your guess: ")

        if guess.lower() =='q':
         print("Thanks for playing GoodByee")
        break
    try:
        guess =int(guess)
    except ValueError:
        print("Invalid input!")
        continue
    attempts +=1

    if guess < numbers:
        print("Too low! Try again.")
    elif guess > numbers: 
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {numbers} correctly in {attempts} attempts!")
    break


Number_guessing_game()