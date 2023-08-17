# We start by importing the random module. This module contains functions for generating random numbers.
import random

# We generate a random number between 1 and 50 and store it in the variable 'number_to_guess'.
number_to_guess = random.randint(1, 50)

# We start a loop that will keep running until we explicitly stop it.
while True:
    # We use a try-except block to handle errors.
    try:
        # We ask the user to guess a number and convert their input to an integer.
        user_guess = int(input("Guess a number between 1 and 50: "))
    # If the user's input can't be converted to an integer, we print an error message and start the loop again.
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # If the user's guess is higher than the number to guess, we tell them it's too high.
    if user_guess > number_to_guess:
        print("Too high, try again.")
    # If the user's guess is lower than the number to guess, we tell them it's too low.
    elif user_guess < number_to_guess:
        print("Too low, try again.")
    # If the user's guess is equal to the number to guess, we congratulate them and stop the loop.
    else:
        print("Congratulations! You guessed the number correctly.")
        break