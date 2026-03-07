# Number Guessing Game

import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")

elif guess > number:
    print("Too high! The correct number was", number)

else:
    print("Too low! The correct number was", number)
