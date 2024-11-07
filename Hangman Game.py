import random

def get_random_word():
    word = ['python', 'hangman', 'programming', 'openai', 'artificial', 'intelligence']
    return random.choice(word)

def display_word(word , guessed_letter):
    return ''.join([letter if letter in guessed_letter else'_' for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome To Hangman!")
    print(f"You have {max_incorrect_guesses} chances to guesses the word.")

    while incorrect_guesses <max_incorrect_guesses:
        print("WOrd to guess:", display_word(word , guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(f"You already guessed '{guess} . Try again")
            continue
        guessed_letters.add(guess)

        if guess in word:
                    
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()


