## Imports random generator function
import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]

## Generates a random word from word_list
word = random.choice(word_list)

## Takes user input and checks if it is a single letter and is alphabetical.
guess = input("Please choose a letter: ")
while guess.isalpha() == False or len(guess) != 1:
    print("Oops! That is not a valid input.")
    guess = input("Please choose a letter: ")
else:
    print("Good guess!")