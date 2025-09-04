# 1 Guessing Game
import random

random_number = random.randint(1,100)
#print(random_number)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > random_number:
        print("Guess is higher.")
    elif guess < random_number:
        print("Guess is lower.")
    else:
        print("Your guesses correctly!")
        break