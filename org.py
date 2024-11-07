import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def load_flashcards():
    # You can add more flashcards or even load them from a file
    flashcards = [
        Flashcard("What is the capital of France?", "Paris"),
        Flashcard("What is the largest planet in our solar system?", "Jupiter"),
        Flashcard("Who wrote 'Hamlet'?", "Shakespeare"),
        Flashcard("What is the square root of 64?", "8"),
        Flashcard("What is the chemical symbol for water?", "H2O")
    ]
    return flashcards

def display_flashcard(flashcard):
    print(f"Question: {flashcard.question}")
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == flashcard.answer.strip().lower():
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is: {flashcard.answer}\n")

def main():
    flashcards = load_flashcards()
    print("Welcome to the Flashcards App!")
    print("Type 'q' to quit at any time.\n")

    while True:
        # Pick a random flashcard
        current_flashcard = random.choice(flashcards)

        display_flashcard(current_flashcard)

        play_again = input("Do you want to continue? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
