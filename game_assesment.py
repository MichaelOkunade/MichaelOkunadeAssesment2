import random
import time
import tkinter as tk
from tkinter import messagebox

def text_based_number_guessing_game():
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

        # Start timer
        start_time = time.time()

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
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 2)
                    print(f"\n🎉 Congratulations! You guessed it!")
                    print("\n📊 Game Summary:")
                    print(f"✅ Correct Number: {number_to_guess}")
                    print(f"🔢 Total Attempts: {attempts}")
                    print(f"🕒 Time Taken: {time_taken} seconds")
                    print(f"📜 Your Guesses: {guess_history}")
                    if high_score is None or attempts < high_score:
                        high_score = attempts
                        print("🏆 New high score!")
                    else:
                        print(f"💡 Current high score: {high_score} attempts")
                    break

            except ValueError:
                print("Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye 👋")
            break

def gui_number_guessing_game():
    # Global high score
    high_score = [None]

    def start_game():
        difficulty = difficulty_var.get()
        if difficulty == 'Easy':
            max_number = 50
        elif difficulty == 'Medium':
            max_number = 100
        elif difficulty == 'Hard':
            max_number = 200
        else:
            max_number = 100

        nonlocal number_to_guess, attempts, guess_history, start_time
        number_to_guess = random.randint(1, max_number)
        attempts = 0
        guess_history = []
        start_time = time.time()

        feedback_label.config(text=f"I'm thinking of a number between 1 and {max_number}.")
        attempts_label.config(text="Attempts: 0")
        time_label.config(text="Time: 0.00 seconds")
        history_label.config(text="Guesses: []")
        correct_label.config(text="")
        guess_entry.config(state='normal')
        guess_entry.delete(0, tk.END)
        submit_button.config(state='normal')
        play_again_button.pack_forget()

    def submit_guess():
        try:
            guess = int(guess_entry.get())
            guess_entry.delete(0, tk.END)
            if guess in guess_history:
                feedback_label.config(text="⚠️ You've already guessed that number! Try a different one.")
                return

            guess_history.append(guess)
            nonlocal attempts
            attempts += 1

            if guess < number_to_guess:
                feedback_label.config(text="Too low! Try again.")
            elif guess > number_to_guess:
                feedback_label.config(text="Too high! Try again.")
            else:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                feedback_label.config(text="🎉 Congratulations! You guessed it!")
                correct_label.config(text=f"Correct Number: {number_to_guess}")
                attempts_label.config(text=f"Total Attempts: {attempts}")
                time_label.config(text=f"Time Taken: {time_taken} seconds")
                history_label.config(text=f"Your Guesses: {guess_history}")
                if high_score[0] is None or attempts < high_score[0]:
                    high_score[0] = attempts
                    high_score_label.config(text="🏆 New high score!")
                else:
                    high_score_label.config(text=f"💡 Current high score: {high_score[0]} attempts")
                guess_entry.config(state='disabled')
                submit_button.config(state='disabled')
                play_again_button.pack()

        except ValueError:
            feedback_label.config(text="Please enter a valid number.")
            guess_entry.delete(0, tk.END)

    def play_again():
        start_game()

    def quit_game():
        root.quit()

    root = tk.Tk()
    root.title("🎯 Number Guessing Game")
    root.geometry("400x500")

    # Difficulty frame
    difficulty_frame = tk.Frame(root)
    difficulty_frame.pack(pady=10)
    tk.Label(difficulty_frame, text="Choose difficulty:", font=("Arial", 12, "bold")).pack()
    difficulty_var = tk.StringVar(value='Medium')
    tk.Radiobutton(difficulty_frame, text="Easy (1-50)", variable=difficulty_var, value='Easy').pack(anchor='w')
    tk.Radiobutton(difficulty_frame, text="Medium (1-100)", variable=difficulty_var, value='Medium').pack(anchor='w')
    tk.Radiobutton(difficulty_frame, text="Hard (1-200)", variable=difficulty_var, value='Hard').pack(anchor='w')

    start_button = tk.Button(root, text="Start Game", command=start_game, bg="green", fg="white")
    start_button.pack(pady=5)

    # Game frame
    game_frame = tk.Frame(root)
    game_frame.pack(pady=10)

    feedback_label = tk.Label(game_frame, text="", font=("Arial", 10))
    feedback_label.pack()

    guess_entry = tk.Entry(game_frame, state='disabled', width=20)
    guess_entry.pack(pady=5)

    submit_button = tk.Button(game_frame, text="Submit Guess", command=submit_guess, state='disabled', bg="blue", fg="white")
    submit_button.pack(pady=5)

    correct_label = tk.Label(game_frame, text="", font=("Arial", 10, "bold"))
    correct_label.pack()

    attempts_label = tk.Label(game_frame, text="Attempts: 0", font=("Arial", 10))
    attempts_label.pack()

    time_label = tk.Label(game_frame, text="Time: 0.00 seconds", font=("Arial", 10))
    time_label.pack()

    history_label = tk.Label(game_frame, text="Guesses: []", font=("Arial", 10))
    history_label.pack()

    high_score_label = tk.Label(game_frame, text="", font=("Arial", 10, "italic"))
    high_score_label.pack()

    play_again_button = tk.Button(game_frame, text="Play Again", command=play_again, bg="orange", fg="white")

    quit_button = tk.Button(root, text="Quit", command=quit_game, bg="red", fg="white")
    quit_button.pack(side='bottom', pady=10)

    # Initialize variables
    number_to_guess = None
    attempts = 0
    guess_history = []
    start_time = None

    root.mainloop()

def game_menu():
    while True:
        print("\n🎮 Game Menu:")
        print("1. Text-Based Number Guessing Game")
        print("2. GUI Number Guessing Game")
        choice = input("Choose an option (1 or 2): ").strip()
        if choice == '1':
            text_based_number_guessing_game()
            break
        elif choice == '2':
            gui_number_guessing_game()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the game menu
game_menu()
