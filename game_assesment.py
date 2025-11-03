import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    high_score = None

    while True:
        # Difficulty selection
        print("\nChoose a difficulty level:")
        print("1. Easy (1–50)")
        print("2. Medium (1–100)")
        print("3. Hard (1–200)")

        difficulty = input("Enter 1, 2, or 3: ").strip()
        if difficulty == '1':
            max_number = 50
        elif difficulty == '2':
            max_number = 100
        elif difficulty == '3':
            max_number = 200
        else:
            print("Invalid choice. Defaulting to Medium.")
            max_number = 100

        number_to_guess = random.randint(1, max_number)
        attempts = 0
        guess_history = []
        print(f"\nI'm thinking of a number between 1 and {max_number}.")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess in guess_history:
                    print("⚠️ You've already guessed that number! Try a different one.")
                    continue

                guess_history.append(guess)
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                    if high_score is None or attempts < high_score:
                        high_score = attempts
                        print("🏆 New high score!")
                    else:
                        print(f"💡 Current high score: {high_score} attempts")
                    break

                print(f"Your guesses so far: {guess_history}")
            except ValueError:
                print("Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye 👋")
            break

# Run the game
number_guessing_game()