
def Ali_Rehan():
    run_loop = True
    while run_loop:
        print("---Basic Arithmetic Calculator---")
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        if operation == '+':
            print("The sum is:", num1 + num2)
        elif operation == '-':
            print("The difference is:", num1 - num2)
        elif operation == '*':
            print("The product is:", num1 * num2)
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("The quotient is:", num1 / num2)
        else:
            print("Invalid operation.")
        do_again = str(input("Do you want to perform another operation? (yes/no): "))
        if do_again == "no":
            run_loop = False
            print("Terminating..........")
        elif do_again == "yes":
            print("Restarting........If you did not enter yes and are wondering why it restarted, then it is your punishment because I told you how and what you were supposed to enter and you did not follow the instructions.")
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
