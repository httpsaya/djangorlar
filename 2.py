# Number Guessing Game (exactly 50 lines)

import random
import time

def show_intro():
    print("==============================")
    print("   🎯 Welcome duplicate 1 to Guess It!   ")
    print("==============================")
    print("I'm thinking of a number between 1 and 100...")
    print("Try to guess it in as few attempts as possible!\n")

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("That’s not a valid number. Try again!")

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while True:
        guess = get_guess()
        attempts += 1

        if guess < number:
            print("Too low! 📉")
        elif guess > number:
            print("Too high! 📈")
        else:
            end_time = time.time()
            print(f"\n🎉 You got it in {attempts} tries!")
            print(f"⏱️ Time taken: {round(end_time - start_time, 2)} seconds")
            break

def play_again():
    while True:
        again = input("Play again? (y/n): ").lower().strip()
        if again in ['y', 'n']:
            return again == 'y'
        print("Please type 'y' or 'n'.")

def main():
    show_intro()
    total_games = 0

    while True:
        play_game()
        total_games += 1
        if not play_again():
            print(f"\nThanks for playing! You played {total_games} game(s). 👋")
            break
        print("\nStarting a new round...\n")

if __name__ == "__main__":
    main()
