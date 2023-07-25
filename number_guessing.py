#Number Guessing Game: Develop a program that generates a random number and allows the user to guess it. 
#Provide hints for higher or lower guesses until the correct number is guessed.
import random

random_integer = random.randint(1, 100)


guess = int(input("What is your guess? "))

while guess != random_integer:
    if guess > random_integer:
        print("You need to guess lower")
        guess = int(input("What is your guess? "))
    elif guess < random_integer:
        print("You need to guess higher")
        guess = int(input("What is your guess? "))
    else:
        print("You guessed correct")
        break
print("You guessed correct!")
