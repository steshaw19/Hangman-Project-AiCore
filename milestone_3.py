## Imports random generator function
import random

word_list = ["apple", "banana", "orange", "blueberry", "fig"]

## Generates a random word from word_list
word = random.choice(word_list)

## Takes user input and checks if it is a single letter and is alphabetical.
guess = input("Please choose a letter: ")

while True:
    if guess in word: 
        print("Good guess - that letter is in the word!\n")
        guess = input("Please choose your next letter: ")
    elif guess not in word:
        print("That's a good guess, but not in this word.\n")
        guess = input("Please choose your next letter: ")
    else:
        if guess.isalpha() == False or len(guess) != 1:
            print("Oops! That is not a valid input.\n")
            guess = input("Please choose a letter: ")