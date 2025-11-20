import random
import time

def Sheharyar_Khalid():
    while True:   # <-- LOOP WRAPS THE ENTIRE GAME (important)
        random.seed(time.time())  # seeds randomness with time
        number = random.randint(1, 50)
        attempts = 0

        print("Guess a number between 1 and 50.")

        while True:
            guess = int(input(f"Enter your guess no. {attempts + 1}: "))
            attempts += 1

            if guess < 1 or guess > 50:
                print("Guess must be between 1 and 50.")
                continue

            if guess > number:
                print("Too high! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break   # exit guessing loop

        # ask to play again
        again = input("Do you want to play again? (y/n): ").strip().lower()

        if again != 'y':
            print("Thank you for playing!")
            break      # exit main game loop and ends program if user enters anything other then 'y'

Sheharyar_Khalid()